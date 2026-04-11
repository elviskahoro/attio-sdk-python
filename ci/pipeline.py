#!/usr/bin/env python3
"""Attio SDK Dagger CI pipeline.

Usage:
    dagger run python ci/pipeline.py generate [--force] [--version VERSION]
"""

import argparse
import asyncio
import os
import sys

import dagger


async def generate(force: bool = False, version: str | None = None) -> None:
    config = dagger.Config(log_output=sys.stderr)
    async with dagger.Connection(config) as dag:
        api_key = dag.set_secret("SPEAKEASY_API_KEY", os.environ["SPEAKEASY_API_KEY"])
        src = dag.host().directory(".")

        run_args = ["speakeasy", "run"]
        if force:
            run_args.append("--force")
        if version:
            run_args += ["--set-version", version]

        await (
            dag.container()
            .from_("ghcr.io/speakeasy-api/speakeasy:latest")
            .with_exec(["/bin/sh", "-c", "sudo apt-get update && sudo apt-get install -y ca-certificates"])
            .with_secret_variable("SPEAKEASY_API_KEY", api_key)
            .with_mounted_directory("/repo", src)
            .with_workdir("/repo")
            .with_exec(["/bin/sh", "-c", "mkdir -p .speakeasy/temp"])
            .with_exec(run_args)
            .directory("/repo/src")
            .export("src")
        )


def main() -> None:
    parser = argparse.ArgumentParser(description="Attio SDK CI pipeline")
    sub = parser.add_subparsers(dest="command", required=True)

    gen = sub.add_parser("generate", help="Generate the SDK via Speakeasy")
    gen.add_argument("--force", action="store_true", help="Force regeneration")
    gen.add_argument("--version", metavar="VERSION", help="Pin SDK to a specific version")

    args = parser.parse_args()
    asyncio.run(generate(args.force, args.version))


if __name__ == "__main__":
    main()
