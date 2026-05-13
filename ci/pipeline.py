#!/usr/bin/env python3
"""Attio SDK Dagger CI pipeline with object-oriented design and snapshots.

Available commands:
    fetch-openapi                  Fetch latest OpenAPI spec and update workflow.yaml
    verify-version <version>       Verify pyproject.toml + _version.py match <version>
    release-bump <version>         Rewrite pyproject.toml + _version.py to <version>
    test                           Run test suite
    build                          Build distribution packages
    generate [--force] [--version] Generate SDK via Speakeasy
    publish [--token]              Build and publish to PyPI
    ci [--force] [--version] [...] Complete workflow: test, generate, build, optionally publish

Examples:
    python ci/pipeline.py fetch-openapi
    python ci/pipeline.py verify-version 0.22.9
    python ci/pipeline.py release-bump 0.22.9
    python ci/pipeline.py test
    python ci/pipeline.py generate --force --version 1.0.0
    python ci/pipeline.py build
    python ci/pipeline.py publish --token <token>
    python ci/pipeline.py ci --publish --token <token>

Or via Dagger directly:
    dagger call attio-sdk-pipeline test
    dagger call attio-sdk-pipeline build
    dagger call attio-sdk-pipeline verify-version --version 0.22.9
    dagger call attio-sdk-pipeline release-bump --version 0.22.9 export --path .
    dagger call attio-sdk-pipeline generate --api-key env:SPEAKEASY_API_KEY
    dagger call attio-sdk-pipeline publish --pypi-token env:PYPI_TOKEN
    dagger call attio-sdk-pipeline ci --api-key env:SPEAKEASY_API_KEY --pypi-token env:PYPI_TOKEN
"""

import argparse
import asyncio
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Annotated

import dagger  # type: ignore[import-untyped]
from dagger import Directory, Doc, dag, function  # type: ignore[import-untyped]

_VERIFY_VERSION_SCRIPT = r"""
import os, pathlib, re, sys, tomllib

expected = os.environ["EXPECTED_VERSION"]
py = tomllib.loads(pathlib.Path("pyproject.toml").read_text())["project"]["version"]
m = re.search(
    r'^__version__\s*:\s*str\s*=\s*"([^"]+)"',
    pathlib.Path("src/attio/_version.py").read_text(),
    re.M,
)
under = m.group(1) if m else "<unset>"
print(f"expected={expected} pyproject={py} _version.py={under}")

fail = False
if py != expected:
    print(f"pyproject.toml version {py} does not match {expected}", file=sys.stderr)
    fail = True
if under != expected:
    print(f"_version.py __version__ {under} does not match {expected}", file=sys.stderr)
    fail = True
if fail:
    sys.exit("Version mismatch. Run scripts/release.sh to bump both files in lockstep.")
"""

_RELEASE_BUMP_SCRIPT = r"""
import os, pathlib, re, sys

version = os.environ["RELEASE_VERSION"]

pyproject = pathlib.Path("pyproject.toml")
text = pyproject.read_text()
new = re.sub(r'^(version\s*=\s*)"[^"]+"', rf'\1"{version}"', text, count=1, flags=re.M)
if new == text:
    sys.exit('Could not find version = "..." in pyproject.toml')
pyproject.write_text(new)

vfile = pathlib.Path("src/attio/_version.py")
text = vfile.read_text()
new = re.sub(
    r'^(__version__\s*:\s*str\s*=\s*)"[^"]+"',
    rf'\1"{version}"',
    text,
    count=1,
    flags=re.M,
)
new = re.sub(
    r'^(__user_agent__\s*:\s*str\s*=\s*"speakeasy-sdk/python )[^ ]+( .+")$',
    rf'\g<1>{version}\g<2>',
    new,
    count=1,
    flags=re.M,
)
if new == text:
    sys.exit('Could not find __version__ in src/attio/_version.py')
vfile.write_text(new)
"""


def _sync_write_spec(spec_path: str, spec_data: dict[str, object]) -> None:
    """Write OpenAPI spec to disk (synchronous)."""
    Path(spec_path).parent.mkdir(parents=True, exist_ok=True)
    Path(spec_path).write_text(json.dumps(spec_data, indent=2))


def _sync_update_workflow(overlay_path: str, spec_path: str) -> None:
    """Update workflow.yaml (synchronous)."""
    import re

    workflow_content = Path(".speakeasy/workflow.yaml").read_text()

    workflow_content = re.sub(
        r"location: openapi/api-[\d]+\.json",
        f"location: {spec_path}",
        workflow_content,
    )
    workflow_content = re.sub(
        r"output: openapi/api-[\d]+-overlay\.json",
        f"output: {overlay_path}",
        workflow_content,
    )

    Path(".speakeasy/workflow.yaml").write_text(workflow_content)


async def fetch_latest_spec() -> str:
    """Fetch the latest OpenAPI spec and update workflow.yaml locally."""
    import httpx

    spec_url = "https://api.attio.com/openapi/api"
    from datetime import timezone

    timestamp = datetime.now(tz=timezone.utc).strftime("%Y%m%d%H%M")
    spec_filename = f"api-{timestamp}.json"
    spec_path = f"openapi/{spec_filename}"

    print(f"Fetching latest OpenAPI spec from {spec_url}...", file=sys.stderr)

    async with httpx.AsyncClient(timeout=30.0, follow_redirects=True) as client:
        response = await client.get(spec_url)
        response.raise_for_status()
        try:
            spec_data = response.json()
        except json.JSONDecodeError as err:
            msg = f"Invalid JSON in spec: {err}"
            raise RuntimeError(msg) from err

    # Write spec and workflow synchronously outside async context
    _sync_write_spec(spec_path, spec_data)
    print(f"Saved spec to {spec_path}", file=sys.stderr)

    overlay_filename = f"api-{timestamp}-overlay.json"
    overlay_path = f"openapi/{overlay_filename}"

    _sync_update_workflow(overlay_path, spec_path)

    print(f"Updated .speakeasy/workflow.yaml to point to {spec_path}", file=sys.stderr)
    return spec_path


class AttioSDKPipeline:
    def __init__(self, source: Directory) -> None:
        """Initialize pipeline with source directory."""
        self.source = source

    @function
    def builder_env(self) -> dagger.Container:
        """Base Python environment with uv and pip cache."""
        pip_cache = dag.cache_volume("pip-cache")
        return (
            dag.container()
            .from_("python:3.11-slim")
            .with_mounted_cache("/root/.cache/pip", pip_cache)
            .with_exec(["pip", "install", "uv"])
            .with_mounted_directory("/repo", self.source)
            .with_workdir("/repo")
        )

    @function
    def dependencies_installed(self, container: dagger.Container) -> dagger.Container:
        """Install project dependencies snapshot."""
        return container.with_exec(["uv", "sync"])

    @function
    async def test(self) -> str:
        """Run test suite."""
        env = self.builder_env()
        deps = self.dependencies_installed(env)
        return await deps.with_exec(["uv", "run", "pytest", "-v"]).stdout()

    @function
    async def verify_version(
        self,
        version: Annotated[
            str,
            Doc("Expected version (no leading 'v')"),
        ],
    ) -> str:
        """Verify pyproject.toml and src/attio/_version.py match the expected version.

        Used by the release workflow before publishing to PyPI to catch tags
        that drift from the in-tree version. Run scripts/release.sh <version>
        to fix any mismatch.
        """
        return await (
            dag.container()
            .from_("python:3.13-slim")
            .with_mounted_directory("/repo", self.source)
            .with_workdir("/repo")
            .with_env_variable("EXPECTED_VERSION", version)
            .with_exec(["python", "-c", _VERIFY_VERSION_SCRIPT])
            .stdout()
        )

    @function
    def release_bump(
        self,
        version: Annotated[
            str,
            Doc("Target version (no leading 'v'), e.g. 0.22.9"),
        ],
    ) -> dagger.Directory:
        """Rewrite pyproject.toml + src/attio/_version.py to the target version.

        Returns the patched repo as a Directory so the caller can export the
        files back to the host (the git commit/tag/push lives in
        scripts/release.sh, not inside the container).
        """
        return (
            dag.container()
            .from_("python:3.13-slim")
            .with_mounted_directory("/repo", self.source)
            .with_workdir("/repo")
            .with_env_variable("RELEASE_VERSION", version)
            .with_exec(["python", "-c", _RELEASE_BUMP_SCRIPT])
            .directory("/repo")
        )

    @function
    def speakeasy_env(self, api_key: dagger.Secret) -> dagger.Container:
        """Speakeasy environment with dependencies."""
        apt_cache = dag.cache_volume("apt-cache")
        return (
            dag.container()
            .from_("ghcr.io/speakeasy-api/speakeasy:latest")
            .with_mounted_cache("/var/cache/apt/archives", apt_cache)
            .with_exec(
                [
                    "/bin/sh",
                    "-c",
                    "sudo apt-get update && sudo apt-get install -y ca-certificates",
                ],
            )
            .with_secret_variable("SPEAKEASY_API_KEY", api_key)
            .with_mounted_directory("/repo", self.source)
            .with_workdir("/repo")
        )

    @function
    def speakeasy_prepared(
        self,
        container: dagger.Container,
    ) -> dagger.Container:
        """Prepare speakeasy container with ownership and temp dir."""
        return container.with_exec(
            ["/bin/sh", "-c", "sudo chown -R speakeasy:speakeasy /repo"],
        ).with_exec(["/bin/sh", "-c", "mkdir -p .speakeasy/temp"])

    @function
    def speakeasy_executed(
        self,
        container: dagger.Container,
        *,
        force: bool = False,
        version: str | None = None,
    ) -> dagger.Container:
        """Execute speakeasy generation."""
        run_args = ["speakeasy", "run"]
        if force:
            run_args.append("--force")
        if version:
            run_args += ["--set-version", version]
        return container.with_exec(run_args)

    @function
    async def generate(
        self,
        api_key: Annotated[dagger.Secret, Doc("Speakeasy API key")],
        *,
        force: Annotated[bool, Doc("Force regeneration")] = False,
        version: Annotated[str | None, Doc("SDK version")] = None,
    ) -> dagger.Directory:
        """Generate SDK via Speakeasy.

        Steps:
        1. Fetch latest OpenAPI spec
        2. Prepare Speakeasy container with API key
        3. Set up ownership and temp directories
        4. Execute generation with optional flags
        5. Export generated source directory
        """
        await fetch_latest_spec()

        env = self.speakeasy_env(api_key)
        prepared = self.speakeasy_prepared(env)
        executed = self.speakeasy_executed(prepared, force=force, version=version)

        await executed.sync()
        return executed.directory("/repo/src")

    @function
    def build(self) -> dagger.Container:
        """Build distribution packages."""
        env = self.builder_env()
        deps = self.dependencies_installed(env)
        return deps.with_exec(["uv", "build"])

    @function
    async def publish(
        self,
        pypi_token: Annotated[dagger.Secret, Doc("PyPI token")],
    ) -> str:
        """Build and publish SDK to PyPI.

        Steps:
        1. Install dependencies
        2. Build distribution packages
        3. Publish to PyPI with token
        """
        built = self.build()
        await (
            built.with_secret_variable("PYPI_TOKEN", pypi_token)
            .with_exec(["/bin/sh", "-c", "uv publish --token $PYPI_TOKEN"])
            .sync()
        )
        return "Published to PyPI"

    @function
    async def ci(
        self,
        api_key: Annotated[dagger.Secret, Doc("Speakeasy API key")],
        pypi_token: Annotated[dagger.Secret, Doc("PyPI token")] | None = None,
    ) -> str:
        """Complete CI workflow: test, generate, build, optionally publish."""
        test_output = await self.test()
        print(f"Tests passed\n{test_output}", file=sys.stderr)

        await self.generate(api_key=api_key)
        print("SDK generated successfully", file=sys.stderr)

        built = self.build()
        await built.sync()
        print("Build completed successfully", file=sys.stderr)

        if pypi_token:
            published = await self.publish(pypi_token=pypi_token)
            return f"Complete CI pipeline finished. {published}"

        return "Complete CI pipeline finished (publish skipped)"


async def cmd_test() -> None:
    """CLI handler for test command."""
    import os

    os.environ.setdefault("DAGGER_PROGRESS", "plain")
    os.environ.setdefault("OTEL_SDK_DISABLED", "true")
    async with dagger.connection(dagger.Config(log_output=sys.stderr)):
        source_dir = dag.host().directory(".")
        pipeline = AttioSDKPipeline(source=source_dir)
        result = await pipeline.test()
        print(result)


async def cmd_generate(*, force: bool, version: str | None) -> None:
    """CLI handler for generate command."""
    import os

    os.environ.setdefault("DAGGER_PROGRESS", "plain")
    os.environ.setdefault("OTEL_SDK_DISABLED", "true")
    async with dagger.connection(dagger.Config(log_output=sys.stderr)):
        api_key_str = os.environ.get("SPEAKEASY_API_KEY")
        if not api_key_str:
            msg = "SPEAKEASY_API_KEY environment variable not set"
            raise RuntimeError(msg) from None

        api_key = dag.set_secret("SPEAKEASY_API_KEY", api_key_str)
        source_dir = dag.host().directory(".")
        pipeline = AttioSDKPipeline(source=source_dir)
        await pipeline.generate(api_key=api_key, force=force, version=version)
        print("SDK generated successfully", file=sys.stderr)


async def cmd_build() -> None:
    """CLI handler for build command.

    Builds inside a container and exports the resulting wheel/sdist back to
    the host's ./dist directory so callers (CI publish step, manual uploads)
    can pick them up.
    """
    import os

    os.environ.setdefault("DAGGER_PROGRESS", "plain")
    os.environ.setdefault("OTEL_SDK_DISABLED", "true")
    async with dagger.connection(dagger.Config(log_output=sys.stderr)):
        source_dir = dag.host().directory(".")
        pipeline = AttioSDKPipeline(source=source_dir)
        built = pipeline.build()
        await built.directory("/repo/dist").export("./dist")
        print("Build completed successfully (artifacts in ./dist)", file=sys.stderr)


async def cmd_publish(*, token: str | None = None) -> None:
    """CLI handler for publish command."""
    import os

    os.environ.setdefault("DAGGER_PROGRESS", "plain")
    os.environ.setdefault("OTEL_SDK_DISABLED", "true")
    async with dagger.connection(dagger.Config(log_output=sys.stderr)):
        token_to_use = token
        if token_to_use is None:
            token_to_use = os.environ.get("PYPI_TOKEN")
            if not token_to_use:
                msg = "PYPI_TOKEN environment variable not set"
                raise RuntimeError(msg) from None

        pypi_secret = dag.set_secret("PYPI_TOKEN", token_to_use)
        source_dir = dag.host().directory(".")
        pipeline = AttioSDKPipeline(source=source_dir)
        result = await pipeline.publish(pypi_token=pypi_secret)
        print(result, file=sys.stderr)


async def cmd_ci(
    *,
    force: bool = False,
    version: str | None = None,
    token: str | None = None,
    publish: bool = False,
) -> None:
    """CLI handler for complete CI workflow."""
    import os

    os.environ.setdefault("DAGGER_PROGRESS", "plain")
    os.environ.setdefault("OTEL_SDK_DISABLED", "true")
    async with dagger.connection(dagger.Config(log_output=sys.stderr)):
        api_key_str = os.environ.get("SPEAKEASY_API_KEY")
        if not api_key_str:
            msg = "SPEAKEASY_API_KEY environment variable not set"
            raise RuntimeError(msg) from None

        api_key = dag.set_secret("SPEAKEASY_API_KEY", api_key_str)

        pypi_secret = None
        if publish:
            token_to_use = token
            if token_to_use is None:
                token_to_use = os.environ.get("PYPI_TOKEN")
            if not token_to_use:
                msg = "PYPI_TOKEN environment variable required for publish"
                raise RuntimeError(msg) from None
            pypi_secret = dag.set_secret("PYPI_TOKEN", token_to_use)

        _ = force
        _ = version
        source_dir = dag.host().directory(".")
        pipeline = AttioSDKPipeline(source=source_dir)
        result = await pipeline.ci(api_key=api_key, pypi_token=pypi_secret)
        print(result, file=sys.stderr)


async def cmd_fetch_openapi() -> None:
    """CLI handler for fetch-openapi command."""
    await fetch_latest_spec()
    print("OpenAPI spec fetched and workflow updated", file=sys.stderr)


async def cmd_verify_version(version: str) -> None:
    """CLI handler for verify-version command."""
    import os

    os.environ.setdefault("DAGGER_PROGRESS", "plain")
    os.environ.setdefault("OTEL_SDK_DISABLED", "true")
    async with dagger.connection(dagger.Config(log_output=sys.stderr)):
        source_dir = dag.host().directory(".")
        pipeline = AttioSDKPipeline(source=source_dir)
        result = await pipeline.verify_version(version=version)
        print(result)


async def cmd_release_bump(version: str) -> None:
    """CLI handler for release-bump command.

    Bumps the version inside a container, then exports the patched files back
    to the host so the caller (scripts/release.sh) can commit, tag, and push.
    """
    import os

    os.environ.setdefault("DAGGER_PROGRESS", "plain")
    os.environ.setdefault("OTEL_SDK_DISABLED", "true")
    async with dagger.connection(dagger.Config(log_output=sys.stderr)):
        source_dir = dag.host().directory(".")
        pipeline = AttioSDKPipeline(source=source_dir)
        patched = pipeline.release_bump(version=version)
        await patched.export(".")
        print(f"Bumped version to {version}", file=sys.stderr)


def main() -> None:
    parser = argparse.ArgumentParser(description="Attio SDK CI pipeline")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser(
        "fetch-openapi",
        help="Fetch latest OpenAPI spec and update workflow.yaml",
    )
    sub.add_parser("test", help="Run test suite")
    sub.add_parser("build", help="Build distribution packages")

    verify = sub.add_parser(
        "verify-version",
        help="Verify pyproject.toml + _version.py match the given version",
    )
    verify.add_argument("version", help="Expected version (no leading 'v')")

    bump = sub.add_parser(
        "release-bump",
        help="Bump pyproject.toml + _version.py to a new version",
    )
    bump.add_argument("version", help="Target version (no leading 'v'), e.g. 0.22.9")

    gen = sub.add_parser("generate", help="Generate the SDK via Speakeasy")
    gen.add_argument("--force", action="store_true", help="Force regeneration")
    gen.add_argument(
        "--version",
        metavar="VERSION",
        help="Pin SDK to a specific version",
    )

    pub = sub.add_parser("publish", help="Build and publish the SDK to PyPI")
    pub.add_argument(
        "--token",
        metavar="TOKEN",
        help="PyPI token (defaults to PYPI_TOKEN env var)",
    )

    ci = sub.add_parser(
        "ci",
        help="Complete CI workflow: test, generate, build, publish",
    )
    ci.add_argument("--force", action="store_true", help="Force SDK regeneration")
    ci.add_argument(
        "--version",
        metavar="VERSION",
        help="Pin SDK to a specific version",
    )
    ci.add_argument(
        "--publish",
        action="store_true",
        help="Publish to PyPI after building",
    )
    ci.add_argument(
        "--token",
        metavar="TOKEN",
        help="PyPI token (defaults to PYPI_TOKEN env var)",
    )

    args = parser.parse_args()

    if args.command == "fetch-openapi":
        asyncio.run(cmd_fetch_openapi())
    elif args.command == "verify-version":
        asyncio.run(cmd_verify_version(version=args.version))
    elif args.command == "release-bump":
        asyncio.run(cmd_release_bump(version=args.version))
    elif args.command == "test":
        asyncio.run(cmd_test())
    elif args.command == "build":
        asyncio.run(cmd_build())
    elif args.command == "generate":
        asyncio.run(cmd_generate(force=args.force, version=args.version))
    elif args.command == "publish":
        asyncio.run(cmd_publish(token=args.token))
    elif args.command == "ci":
        asyncio.run(
            cmd_ci(
                force=args.force,
                version=args.version,
                token=args.token,
                publish=args.publish,
            ),
        )


if __name__ == "__main__":
    main()
