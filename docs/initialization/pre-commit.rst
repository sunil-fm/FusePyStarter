=======================
Pre-commit Integration
=======================

.. contents::
   :local:
   :depth: 2

Introduction
============

**Pre-commit** is a multi-language package manager for Git hooks. It ensures code quality by running defined checks automatically on every commit. This prevents issues like syntax errors, trailing whitespace, or incorrect commit messages from entering your repository.

For full documentation, visit: https://pre-commit.com/

Why Use Pre-commit?
-------------------

- Catches issues early (before CI/CD).
- Improves code consistency and quality.
- Reduces reviewer fatigue over trivial issues.
- Enforces standards across teams.
- Easy to configure and share.

Installation
============

.. code-block:: console

   $ uv add --dev pre-commit
   $ pre-commit install

This installs the Git hook scripts and sets up .git/hooks/pre-commit.

Optional (Auto-enable for all repos):

.. code-block:: console

   $ git config --global init.templateDir ~/.git-template
   $ pre-commit init-templatedir ~/.git-template

Configuration
=============

Create a file named .pre-commit-config.yaml in the root of your project. Here's an example setup:

.. literalinclude:: ../../.pre-commit-config.yaml
   :language: yaml
   :caption: .pre-commit-config.yaml

Hook Categories
===============

General Code Hygiene
--------------------

- **check-added-large-files**: Prevent committing files over 500 KB.
- **trailing-whitespace**: Strips trailing spaces from lines (runs in pre-commit, pre-push, and manual stages).
- **end-of-file-fixer**: Ensures files end with a newline (excludes Python files).
- **mixed-line-ending**: Converts inconsistent line endings to LF.
- **detect-private-key**: Warns if a private key is accidentally committed.

Syntax and Format Validation
----------------------------

- **check-ast**: Ensures Python code is valid syntax.
- **check-json**, **check-yaml**, **check-toml**: Validates file syntax (YAML check runs with --unsafe flag).
- **check-case-conflict**: Checks for filename conflicts on case-insensitive filesystems.
- **check-merge-conflict**: Prevents merge conflict markers from being committed.

Python-Specific Quality
-----------------------

- **ruff**: Linting and static analysis with fixes enabled (targets Python 3.12, ignores E203).
- **ruff-format**: Formats code to Python 3.12 standards.
- **mypy**: Type-checks Python code with --disallow-untyped-defs (excludes docs directory).
- **add-trailing-comma**: Adds trailing commas to Python collections (Python 3.6+ compatible).
- **debug-statements**: Prevents committing Python breakpoint() or pdb calls.
- **pydoclint**: Enforces Google-style docstrings with strict validation:
  - Checks argument order and type hints
  - Validates return and yield sections
  - Verifies class attributes documentation
  - Ensures style consistency
- **flake8**: Additional docstring checks (Google style convention) focused on src/ directory.

Git and Commit Message Hooks
----------------------------

- **no-commit-to-branch**: Prevents commits to protected branches (main/master).
- **conventional-pre-commit**: Strict validation of commit messages against Conventional Commits:
  - Enforces types: feat, fix, chore, refactor, docs, style, test, perf, ci, build, revert
  - Requires scope
  - Runs at commit-msg stage

UV Lockfile Integrity
---------------------

- **uv-lock**: Ensures uv-generated lockfiles are up-to-date and correct.

Usage
=====

Pre-commit hooks will run automatically on each git commit.

To manually run all hooks:

.. code-block:: console

   $ pre-commit run --all-files

To run on specific files:

.. code-block:: console

   $ pre-commit run --files path/to/file1.py path/to/file2.py

To run a specific hook:

.. code-block:: console

   $ pre-commit run <hook-id>

Example:

.. code-block:: console

   $ pre-commit run ruff --all-files

To skip hooks temporarily:

.. code-block:: console

   $ SKIP=ruff git commit -m "chore: skip ruff temporarily"

To update all hooks to latest compatible versions:

.. code-block:: console

   $ pre-commit autoupdate

Maintenance Tips
================

- Run pre-commit autoupdate regularly to keep hooks up-to-date.
- Review .pre-commit-config.yaml and clean up unused hooks as needed.
- Some hooks (like trailing-whitespace) support multiple stages (pre-commit, pre-push, manual).
- For Python projects, maintain consistency between Ruff, mypy, and pydoclint configurations.

Best Practices
==============

- Make pre-commit mandatory in team workflows (e.g., through CI).
- Never bypass conventional-pre-commit without valid reason.
- Combine with EditorConfig for consistent formatting.
- Use Ruff as the primary linter with mypy for type checking.
- Enforce comprehensive docstrings with pydoclint's Google style checks.
- Ensure developers install hooks with pre-commit install after cloning.

Troubleshooting
===============

- **Hook failed**? Run with --all-files to debug.
- **Permissions error**? Ensure Python and pre-commit are installed in your environment.
- **Hook not running**? Confirm .git/hooks/pre-commit exists and is executable.
- **Need debugging info?**

.. code-block:: console

   $ pre-commit run --all-files -v

- **Docstring issues**? Check both pydoclint and flake8-docstrings outputs.
- **Type checking errors**? Verify mypy configuration matches project standards.

Conclusion
==========

Pre-commit is a powerful automation tool that keeps your codebase clean and standardized. The current configuration provides:
- Robust Python quality checks (Ruff, mypy, pydoclint)
- Comprehensive docstring validation
- Strict commit message conventions
- File integrity and syntax verification
By integrating these checks early in your development lifecycle, you ensure consistency and reduce code review burdens.
