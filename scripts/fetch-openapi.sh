#!/usr/bin/env bash
set -euo pipefail

SPEC_URL="https://api.attio.com/openapi/api"
REPO_ROOT="$(git rev-parse --show-toplevel)"
OPENAPI_DIR="${REPO_ROOT}/openapi"
TIMESTAMP="$(date -u +%Y%m%d%H%M)"
OUTFILE="${OPENAPI_DIR}/api-${TIMESTAMP}.json"

mkdir -p "$OPENAPI_DIR"

echo "Downloading Attio OpenAPI spec..."
curl -sf "$SPEC_URL" | python3 -m json.tool > "$OUTFILE"

echo "Saved to: ${OUTFILE}"

# Update workflow.yaml to point to the new spec
RELATIVE="openapi/api-${TIMESTAMP}.json"
OVERLAY_RELATIVE="openapi/api-${TIMESTAMP}-overlay.json"

sed -i '' "s|location: openapi/api-.*\.json|location: ${RELATIVE}|" "${REPO_ROOT}/.speakeasy/workflow.yaml"
sed -i '' "s|output: openapi/api-.*\.json|output: ${OVERLAY_RELATIVE}|" "${REPO_ROOT}/.speakeasy/workflow.yaml"

echo "Updated .speakeasy/workflow.yaml:"
echo "  input:  ${RELATIVE}"
echo "  output: ${OVERLAY_RELATIVE}"
echo ""
echo "Next steps:"
echo "  1. Review the new spec for changes"
echo "  2. Verify overlay.yaml targets still apply to the new spec"
echo "  3. Run 'speakeasy run' to regenerate the SDK"
