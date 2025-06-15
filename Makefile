.PHONY: lint test check coverage

lint:
	uv run ruff check .

test:
	uv run pytest -q

check: lint test

coverage:
	uv run pytest --cov=gendiff --cov-report=xml
