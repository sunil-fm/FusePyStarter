=====================
Testing: pytest-cov
=====================

Introduction
------------

**pytest-cov** is a plugin for `pytest` that integrates `coverage.py` into the test runner. It enables you to run tests and collect code coverage in one unified command, making it easier to ensure your code is thoroughly tested.

It solves common issues like subprocess tracking, test path mismatches, and manual coverage invocation.

Docs: https://pytest-cov.readthedocs.io/en/latest/readme.html

Key Features
------------

- Automatically collects test coverage with `pytest`
- Supports subprocess tracking
- Compatible with `coverage.py` configuration and CLI flags
- Offers terminal, HTML, XML, and JSON coverage reports
- Plays well with tools like `tox`, `pre-commit`, and CI pipelines

Installation
------------

Install as a development dependency using `uv`:

.. code-block:: console

    uv add --dev pytest-cov

.. note::

    You can simplify your toolchain by relying only on `pytest-cov` instead of separately installing `coverage`.

Configuration
-------------

Add the following to your `pyproject.toml` to make coverage reporting automatic:

.. code-block:: toml

    [tool.pytest.ini_options]
    testpaths = ["tests"]
    addopts = "--cov --cov-report=term-missing"

This makes `pytest` automatically collect and show coverage in the terminal.

Usage
-----

Basic coverage collection:

.. code-block:: console

    pytest --cov

Show missing lines in the terminal:

.. code-block:: console

    pytest --cov --cov-report=term-missing

Skip fully covered files from the terminal report:

.. code-block:: console

    pytest --cov --cov-report=term-missing:skip-covered

Generate an interactive HTML report:

.. code-block:: console

    pytest --cov --cov-report=html
    brave-browser htmlcov/index.html

This will open the visual coverage report from the `htmlcov/` folder in your browser.

Additional Resources
--------------------

- Plugin homepage: https://pypi.org/project/pytest-cov/
- Docs: https://pytest-cov.readthedocs.io/en/latest/
- Coverage reference: https://coverage.readthedocs.io/en/latest/

Next Step
---------

Use **tox** to automate multi-environment testing and standardized test workflows. This allows you to run linting, testing, and packaging across different Python versions and configurations.

Uninstall
---------

To remove `pytest-cov` from your environment:

.. code-block:: console

    uv remove --dev pytest-cov
