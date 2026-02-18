.PHONY: build publish publish-test test clean docs docs-serve

build: clean
	uv build

publish-test: build
	uv publish --publish-url https://test.pypi.org/legacy/

publish: build
	uv publish

test:
	uv run pytest

clean:
	rm -rf dist/

docs:
	uv run --group docs mkdocs build

docs-serve:
	uv run --group docs mkdocs serve
