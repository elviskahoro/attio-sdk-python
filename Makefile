.PHONY: build publish bump-patch bump-minor bump-major test clean help

help:
	@echo "Available commands:"
	@echo "  build       - Build the package"
	@echo "  publish     - Build and publish to PyPI (requires PYPI_TOKEN)"
	@echo "  bump-patch  - Bump patch version using Speakeasy"
	@echo "  bump-minor  - Bump minor version using Speakeasy"
	@echo "  bump-major  - Bump major version using Speakeasy"
	@echo "  test        - Run tests"
	@echo "  clean       - Clean build artifacts"
	@echo ""
	@echo "Usage: make publish PYPI_TOKEN=your_token_here"

build:
	uv build

publish: build
	@if [ -z "$(PYPI_TOKEN)" ]; then \
		echo "Error: PYPI_TOKEN is required. Usage: make publish PYPI_TOKEN=your_token_here"; \
		exit 1; \
	fi
	uv publish --token $(PYPI_TOKEN)

bump-patch:
	speakeasy bump patch

bump-minor:
	speakeasy bump minor

bump-major:
	speakeasy bump major

test:
	uv run pytest

clean:
	rm -rf dist/
	rm -rf build/
	rm -rf *.egg-info/