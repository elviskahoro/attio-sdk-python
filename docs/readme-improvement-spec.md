# README Improvement Spec

## Objective

Make `README.md` the fastest path for a Python developer to successfully use this SDK in production.

## Current State Findings

1. SDK generation is managed by Speakeasy via:
   - `.speakeasy/workflow.yaml`
   - `.speakeasy/gen.yaml`
   - `speakeasy run`
2. Generated SDK/API reference files are overwritten on generation:
   - `src/attio/**`
   - `docs/models/**`
   - `docs/errors/**`
   - `docs/sdks/**`
3. `README.md` is not listed in `.speakeasy/gen.lock` tracked files and was not modified during a local `speakeasy run` validation.
4. `README.md` currently contains low-value boilerplate that is not helpful for first-use success.

## Ownership and Overwrite Rules

Treat these files as generated and non-authoritative for manual docs:
- `src/attio/**`
- `docs/models/**`
- `docs/errors/**`
- `docs/sdks/**`
- `.speakeasy/gen.lock`

Treat these files as safe for durable custom documentation:
- `README.md`
- `docs/readme-improvement-spec.md`
- Any new `docs/readme/` authored content files

Rule: never place important hand-written guidance inside generated SDK source/doc files.

## Target Audience

Primary audience: Python developers integrating Attio for the first time.

They should be able to complete these tasks from the README alone:
1. Install the package correctly.
2. Authenticate and create an SDK client.
3. Make a first successful API call.
4. Understand sync vs async usage.
5. Handle errors and retries.
6. Find the exact operation-level docs quickly.

## Content Principles

1. Optimize for task completion, not boilerplate.
2. Keep conceptual text short; prefer runnable examples.
3. Use Attio-specific examples (objects/records/lists), not generic placeholders.
4. Keep API surface exhaustive docs linked, not duplicated.
5. Remove marketing/vendor attribution sections that do not help usage.

## Content to Remove

Remove and prevent reintroduction of:
1. `Development` / `Maturity` prose in README.
2. `Contributions` boilerplate in README.
3. `SDK Created by Speakeasy` footer in README.

If contribution guidance is needed, keep it in `CONTRIBUTING.md`, not README.

## Proposed README Information Architecture

1. Title + one-line value proposition
2. Installation (`uv`, `pip`, `poetry`) with real package commands
3. Authentication setup
4. 60-second quickstart (sync and async)
5. Common workflows
   - List objects
   - Create/update a record
   - Query records
6. Error handling and retries
7. Pagination and filtering patterns (where applicable)
8. Resource lifecycle and client reuse
9. Link hub
   - Full API reference (`docs/sdks/**`)
   - Model/error references
   - Attio official API docs

## Implementation Plan

1. Rewrite top-level README sections for first-use flow.
2. Keep generated operation listings, but move them behind clear “Full API Reference” framing.
3. Replace placeholder install commands (`git+<UNSET>.git`) with actual install guidance.
4. Add 2-3 Attio-specific end-to-end examples with copy/paste-ready code.
5. Add a short troubleshooting section (auth failures, missing scopes, validation errors).

## Acceptance Criteria

This effort is complete when:
1. A new user can run install + first request in under 5 minutes using README only.
2. README has no non-actionable boilerplate sections.
3. README changes persist across `speakeasy run`.
4. README links to operation docs remain valid.

## Non-Goals

1. Duplicating full operation-level reference in README.
2. Editing generated SDK internals for documentation wording.
3. Replacing generated `docs/sdks/**` with custom hand-written operation docs.
