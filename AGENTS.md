# AGENTS.md — tp-intro

## Project

Python exercise repo (`tp-intro`) for an OpenCode hands-on TP. Single module: `toolbox.py`.

## Toolchain

- **Python 3.14**, managed by `uv`. Install deps: `uv sync`
- **Lint/format**: `ruff`
- **Test**: `pytest` — run all: `pytest`. Run a single test: `pytest -k test_is_palindrome_with_spaces`

## Workflow

- **TDD**: write tests first, then implement. Verify with `pytest` after each change.
- **Clean code**: readable names, single-responsibility functions, no dead code.
- Run `ruff check toolbox.py` before committing.

## Known state

- `is_palindrome` has an intentional bug: spaces are not stripped before comparison. `test_is_palindrome_with_spaces` fails by design.
- `word_frequency` and `celsius_to_fahrenheit` raise `NotImplementedError` — these are the implementation tasks in the TP.
