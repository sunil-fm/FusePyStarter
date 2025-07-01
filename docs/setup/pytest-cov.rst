=====================
Testing: pytest-cov
=====================

**pytest-cov** is a powerful `pytest` plugin that integrates seamlessly with `coverage.py`
to generate test coverage reports. It provides:

- **Subprocess support** – Tracks coverage across subprocesses automatically.
- **Better `pytest` integration** – Prevents issues like path mismatches with `coverage run -m pytest`.
- **Full support for coverage configuration and reporting**.

All functionality from the `coverage` package is supported and can be customized via
command-line flags or `pyproject.toml`.

📚 For complete reference, visit the
`official docs <https://pytest-cov.readthedocs.io/en/latest/readme.html>`_.

Installation
============

Install as a development dependency using `uv`:

.. code-block:: console

    $ uv add --dev pytest-cov

.. note::

    You can replace both ``pytest`` and ``coverage`` with ``pytest-cov`` in your
    development dependencies for a simpler and more unified setup.

Usage
=====

Basic usage to collect coverage:

.. code-block:: console

    $ pytest --cov

Show missing lines directly in terminal output:

.. code-block:: console

    $ pytest --cov --cov-report=term-missing

Skip fully covered files from the terminal report:

.. code-block:: console

    $ pytest --cov --cov-report=term-missing:skip-covered

Generate an HTML report with annotated source files:

.. code-block:: console

    $ pytest --cov --cov-report=html
    $ brave-browser htmlcov/index.html

.. note::

    The HTML report will be saved in the ``htmlcov/`` directory. You can open it using
    your preferred web browser.

Configuration
=============

To apply coverage options automatically for all test runs, configure `pytest` via `pyproject.toml`:

.. code-block:: toml

    [tool.pytest.ini_options]
    testpaths = ["tests"]
    addopts = "--cov --cov-report=term-missing"

This ensures that all test executions include coverage reporting by default.

Uninstallation
==============

To remove `pytest-cov` from your environment:

.. code-block:: console

    $ uv remove --dev pytest-cov
