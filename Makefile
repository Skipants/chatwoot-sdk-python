.PHONY: build publish publish-test test clean

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
