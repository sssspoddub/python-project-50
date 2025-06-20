.PHONY: lint test check test-coverage

lint:
	uv run ruff check .

test:
	uv run pytest -q

test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml --cov-fail-under=80

check: lint test

fix:
	uv run ruff check --fix .