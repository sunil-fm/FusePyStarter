=======================
Pre-commit Integration
=======================

Introduction
------------

**Pre-commit** is a framework for managing and maintaining multi-language Git hooks. It automates code quality checks before a commit is accepted, helping enforce standards, catch errors early, and reduce trivial issues in code reviews.

Why use pre-commit?

- Catch errors before code reaches CI
- Enforce consistent code styles
- Validate file syntax, size, and structure
- Ensure type and docstring correctness
- Block commits that violate team policies

Key Features
------------

- Runs checks automatically on `git commit`
- Supports Python and non-Python checks
- Enforces linting, formatting, typing, and docstring style
- Blocks dangerous or large file commits
- Validates YAML, JSON, TOML syntax
- Ensures commit messages follow Conventional Commit rules

Installation
------------

Install `pre-commit`:

.. code-block:: bash

    uv add --dev pre-commit
    pre-commit install

This sets up Git hooks in `.git/hooks/pre-commit` and ensures checks run automatically.

Optional: Apply globally to all Git repos:

.. code-block:: bash

    git config --global init.templateDir ~/.git-template
    pre-commit init-templatedir ~/.git-template

Configuration
-------------

Create a `.pre-commit-config.yaml` at your project root. Your current setup includes:

- **General Hygiene Hooks**:
  - `check-added-large-files`: Prevents committing files > 500KB
  - `trailing-whitespace`: Removes trailing spaces
  - `end-of-file-fixer`: Ensures final newline (skips `.py`)
  - `mixed-line-ending`: Converts line endings to LF
  - `check-merge-conflict`: Blocks merge conflict markers
  - `check-case-conflict`, `check-json`, `check-yaml`, `check-toml`

- **Python-Specific Hooks**:
  - `ruff`: Linting with auto-fix and Python 3.12 target
  - `ruff-format`: Consistent formatting
  - `mypy`: Type checks excluding `docs/` and `tests/`
  - `debug-statements`: Blocks `breakpoint()` and `pdb`
  - `pydoclint`: Enforces Google-style docstrings
  - `flake8`: Validates docstrings in `src/`

- **Git & Commit Message Hooks**:
  - `no-commit-to-branch`: Prevents direct commits to `main`/`master`
  - `conventional-pre-commit`: Validates commit messages with required type and scope

- **Project Integrity**:
  - `uv-lock`: Ensures `uv` lockfile integrity
  - `install-dependencies`: Runs `uv pip install -e .`
  - `test`: Runs tests via `uv run pytest`

Usage
-----

Hooks run automatically on `git commit`.

Run all hooks manually:

.. code-block:: bash

    pre-commit run --all-files

Run on specific files:

.. code-block:: bash

    pre-commit run --files path/to/file1.py path/to/file2.py

Run a specific hook:

.. code-block:: bash

    pre-commit run ruff --all-files

Skip a hook:

.. code-block:: bash

    SKIP=ruff git commit -m "chore(ruff): skip ruff temporarily"

Update hook versions:

.. code-block:: bash

    pre-commit autoupdate

Additional Resources
--------------------

- Official Docs: https://pre-commit.com/
- Example Hooks: https://github.com/pre-commit/pre-commit-hooks


Next Step
---------

After setting up `pre-commit`, the next step is to configure **Dynaconf** for managing your application settings and environment configurations. Dynaconf simplifies handling multiple environments, secrets, and layered configurations.

See the next documentation section on Dynaconf configuration to get started.

Uninstall
---------

To remove pre-commit from your project:

.. code-block:: bash

    pre-commit uninstall
    uv remove --dev pre-commit

To delete all hook caches:

.. code-block:: bash

    pre-commit clean
