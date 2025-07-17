======================================
Continuous Integration: GitHub Actions
======================================

Introduction
============

**GitHub Actions** provides powerful automation for your software development lifecycle—
right from your repository. Whether you're looking to run unit tests, perform linting,
build packages, or deploy applications, GitHub Actions allows you to define custom
workflows triggered by GitHub events like pushes and pull requests.

For more information, visit the official documentation:
https://docs.github.com/en/actions

Key Features
============

- **Event-based triggers**: Automatically run workflows on ``push``, ``pull_request``, or schedules.
- **Matrix builds**: Easily test across multiple Python versions or environments.
- **Reusable actions**: Compose workflows using pre-built or custom actions.
- **Parallel jobs**: Speed up CI pipelines by running steps in parallel.
- **Flexible environment setup**: Easily install tools like ``uv``, ``tox``, and ``pre-commit``.

Installation
============

To get started, make sure your project is hosted on GitHub and contains a
``.github/workflows/`` directory in the root.

Also ensure the following tools are configured in your project:

- ``tox`` for managing and running test environments.
- ``pre-commit`` with a valid ``.pre-commit-config.yaml``.
- ``uv`` via the official ``astral-sh/setup-uv`` GitHub Action.

Configuration
=============

Sample Configurations
---------------------

Place the following files under ``.github/workflows/`` in your repository.

**Pre-Merge Checks: ``pre-merge-tests.yml``**

.. code-block:: yaml

    name: Pre-Merge Checks

    on:
      push:
        branches-ignore:
          - main
      pull_request:
        branches-ignore:
          - main

    jobs:
      test:
        runs-on: ubuntu-latest

        strategy:
          matrix:
            python-version: [3.12, 3.13]

        steps:
          - uses: actions/checkout@v4

          - name: Install UV
            uses: astral-sh/setup-uv@v5
            with:
              version: "0.7.9"

          - name: Set up Python ${{ matrix.python-version }}
            uses: actions/setup-python@v5
            with:
              python-version: ${{ matrix.python-version }}

          - name: Install Dependencies
            run: uv sync

          - name: Run Pre-commit
            uses: pre-commit/action@v3.0.1

          - name: Run tests with Tox
            run: uv run tox -e py

**Main Branch Integrity: ``main-tests.yml``**

.. code-block:: yaml

    name: Main Branch Integrity

    on:
      push:
        branches:
          - main
      pull_request:
        branches:
          - main

    jobs:
      test:
        runs-on: ubuntu-latest

        strategy:
          matrix:
            python-version: [3.12, 3.13]

        steps:
          - uses: actions/checkout@v4

          - name: Install UV
            uses: astral-sh/setup-uv@v5
            with:
              version: "0.7.9"

          - name: Set up Python ${{ matrix.python-version }}
            uses: actions/setup-python@v5
            with:
              python-version: ${{ matrix.python-version }}

          - name: Install Dependencies
            run: uv sync

          - name: Run Pre-commit
            env:
              SKIP: no-commit-to-branch
            uses: pre-commit/action@v3.0.1

          - name: Run tests with Tox
            run: uv run tox -e py

Usage
=====

1. Create the workflow files as shown above.
2. Commit and push the changes to your GitHub repository.
3. Visit the **Actions** tab on GitHub to monitor workflow runs.
4. Create a pull request from a feature branch to ``main`` and observe CI in action.
5. Push directly to ``main`` to validate production-readiness.

Additional Resources
====================

- GitHub Actions: https://docs.github.com/en/actions
- Setup UV Action: https://github.com/astral-sh/setup-uv
- Pre-commit GitHub Action: https://github.com/pre-commit/action
- Tox Documentation: https://tox.readthedocs.io/en/latest/

Next Step
=========

Once you've validated your CI workflows, the next step is to host your project
documentation using **GitHub Pages**. This allows your users and contributors
to access your docs via a public web URL.

Consider using documentation generators like **Sphinx** or **MkDocs** to create
and publish professional-looking documentation.
