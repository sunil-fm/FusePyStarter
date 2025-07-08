==============================
Document Hosting: GitHub Pages
==============================

Introduction
============

This guide walks you through setting up **GitHub Pages** to host your project documentation built with **Sphinx**.

Key Features
============

- Host static HTML docs using GitHub Pages
- Generate documentation with Sphinx + Makefile
- Automate with GitHub Actions
- Easy deployment from `main` branch

Installation
============

First, make sure the following tools are installed:

- Python (>=3.7)
- `uv` — used for dependency management
- Sphinx — documentation generator

To install `uv` (recommended):

.. code-block:: bash

    curl -LsSf https://astral.sh/uv/install.sh | sh

Configuration
=============

Makefile
--------

We have to execute quite a number of commands to generate the docs. To make this process easier, let's create a `Makefile`.

.. code-block:: text

    .PHONY: help docs
    .DEFAULT_GOAL := help


    define BROWSER_PYSCRIPT
    import os, webbrowser, sys

    from urllib.request import pathname2url

    webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
    endef
    export BROWSER_PYSCRIPT

    define PRINT_HELP_PYSCRIPT
    import re, sys

    for line in sys.stdin:
        match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
        if match:
            target, help = match.groups()
            print("%-20s %s" % (target, help))
    endef
    export PRINT_HELP_PYSCRIPT

    BROWSER := python -c "$$BROWSER_PYSCRIPT"

    help:  ## Show this help message
        @python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

    docs:  ## generate Sphinx HTML documentation, including API docs
        rm -f docs/src*.rst
        sphinx-apidoc -o docs/ src
        $(MAKE) -C docs clean
        $(MAKE) -C docs html
        $(BROWSER) docs/_build/html/index.html

GitHub Actions Workflow
-----------------------

Add the following to `.github/workflows/gh-pages.yml`:

.. code-block:: yaml

    name: Documentation

    on:
    push:
        branches:
        - main

    jobs:
    document:
        runs-on: ubuntu-latest

        steps:
        - uses: actions/checkout@v4

        - name: Set up Python
            uses: actions/setup-python@v5
            with:
            python-version: "3.13"

        - name: Install dependencies
            run: |
            python -m pip install --upgrade pip
            pip install sphinx-rtd-theme toml

        - name: Generate Docs
            run: make docs

        - name: Deploy docs to GitHub Pages
            uses: peaceiris/actions-gh-pages@v4
            with:
            github_token: ${{ secrets.GITHUB_TOKEN }}
            publish_dir: docs/_build/html
            allow_empty_commit: true
            keep_files: true

Usage
=====

1. Commit and push the changes to a branch.
2. Create a pull request and merge it into `main`.
3. Once merged, go to the **Actions** tab and verify the `Documentation` job succeeds.
4. Then:
   - Go to your repository **Settings**
   - Scroll to **GitHub Pages**
   - Set **Source** to `Branch: gh-pages`
   - Click **Save**
   - Your docs should now be live at:
     - Available at: https://sunil-fm.github.io/FusePyStarter/

Additional Resources
====================

- `Creating a GitHub Pages site <https://docs.github.com/en/free-pro-team@latest/github/working-with-github-pages/creating-a-github-pages-site>`_

Next Step
=========

Next, we will prepare to publish the package to PyPI. 🎯
