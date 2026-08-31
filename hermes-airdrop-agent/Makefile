PY ?= python3
VENV ?= .venv

.PHONY: help install dev test lint doctor plan report clean

help:
	@echo "make install   one-click install (Hermes + Camofox + haa)"
	@echo "make dev       local venv + package + tests (no system changes)"
	@echo "make test      run the test suite"
	@echo "make doctor    health check"
	@echo "make plan      what is due today"
	@echo "make report    weekly rollup"
	@echo "make clean     remove build artifacts (never touches data/)"

install:
	./install.sh

dev:
	bash scripts/setup.sh

test:
	$(PY) -m pytest

lint:
	@command -v shellcheck >/dev/null && shellcheck install.sh scripts/*.sh || \
		echo "shellcheck not installed — ran bash -n instead" && \
		for f in install.sh scripts/*.sh; do bash -n "$$f" || exit 1; done
	$(PY) -m compileall -q src tests

doctor:
	haa doctor

plan:
	haa plan

report:
	haa report --days 7

clean:
	rm -rf .pytest_cache .mypy_cache build dist *.egg-info
	find . -name __pycache__ -type d -prune -exec rm -rf {} +
