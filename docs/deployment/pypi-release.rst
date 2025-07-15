=====================
Package Hosting: PyPI
=====================

Introduction
============
PyPI (Python Package Index) is the official package repository for Python software. This guide provides comprehensive instructions for packaging, distributing, and maintaining Python projects on PyPI using modern development practices. The documentation covers the complete workflow from project configuration to automated publishing, including security best practices for package distribution.

Key Features
============
- **Hatch-based Build System**: Optimized configuration for PyPI-compatible packages
- **Automated Publishing**: GitHub Actions workflow for seamless PyPI releases
- **Dual Repository Support**: Simultaneous publishing to PyPI and TestPyPI
- **Version Management**: Dynamic version control synced with PyPI releases
- **Security**: Token-based authentication with proper secret management
- **Compatibility**: Broad Python version support (3.8 through 3.13)

Installation
============
To install the package from PyPI:

.. code-block:: console

    pip install fusepystarter

For development installation:

.. code-block:: console

    pip install -i https://test.pypi.org/simple/ fusepystarter

Configuration
=============
PyPI Project Setup
-----------------
Configure your package in ``pyproject.toml``:

.. code-block:: cfg

    [build-system]
    requires = ["hatchling"]
    build-backend = "hatchling.build"

    [project]
    name = "fusepystarter"
    description = "A modern Python project forge with pre-configured tooling and CI/CD."
    dynamic = ["version"]
    authors = [{ name = "Sunil Ghimire", email = "sunil.ghimire@fusemachines.com" }]
    readme = "README.rst"
    requires-python = ">=3.12"
    dependencies = ["dynaconf>=3.2.11", "fire>=0.7.0"]

Build Configuration
-------------------
.. code-block:: cfg

    [tool.hatch.build.targets.sdist]
    exclude = ["/.github", "/docs", "/tests"]

    [tool.hatch.build.targets.wheel]
    packages = ["src"]

    [tool.hatch.version]
    path = "src/__init__.py"

    [tool.hatch]
    installer = "uv"

Token Setup
-----------
1. Create or log in to your PyPI account
2. Navigate to **Account Settings**
3. Select **Add API token**
4. Configure token with appropriate scope
5. Store the token securely

**Security Note**: Treat API tokens as sensitive credentials. They provide full publishing access to your PyPI account.

Usage
=====
Publishing Workflow
-------------------
1. Add PyPI tokens to GitHub Secrets:
   - ``PYPI_TOKEN`` for production
   - ``TEST_PYPI_TOKEN`` for testing environment

2. Use the automated GitHub Actions workflow:

.. code-block:: YAML

    name: PyPI Release

    on:
      push:
        tags:
          - "v*.*.*"

    jobs:
      publish:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v4
          - uses: pypa/hatch@install
          - run: hatch build --clean
          - run: hatch publish
            env:
              HATCH_INDEX_USER: __token__
              HATCH_INDEX_AUTH: ${{ secrets.PYPI_TOKEN }}

Tagging Releases
----------------
Create versioned releases with Git tags:

.. code-block:: console

    git tag v1.0.0
    git push origin v1.0.0

Manual Publishing
-----------------
For manual publishing:

.. code-block:: console

    hatch build
    hatch publish --repo test  # For TestPyPI
    hatch publish             # For PyPI

Additional Resources
====================
- `PyPI Packaging Guide <https://packaging.python.org>`_
- `Hatch Documentation <https://hatch.pypa.io>`_
- `TestPyPI User Guide <https://test.pypi.org>`_
- `Python Packaging Authority <https://www.pypa.io>`_

Next Steps
==========
Once you've tested your package workflows, the next step is to report issues or suggest improvements using our GitHub issue template. This helps us track and address problems systematically.
