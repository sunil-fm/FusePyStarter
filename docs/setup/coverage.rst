=======================
Testing: Coverage (CLI)
=======================

Introduction
------------

**Coverage.py** is a tool for measuring code coverage of Python programs. It tracks which parts of your code are executed while tests run, helping you identify untested areas. This insight ensures your tests are meaningful and thorough.

More info: https://coverage.readthedocs.io/

Key Features
------------

- Tracks statement and branch coverage
- Highlights untested lines in reports
- Supports output in terminal, HTML, XML, JSON
- Integrates with `pytest`, `unittest`, and others
- Configurable via `pyproject.toml`
- Optionally fails builds below a coverage threshold

Installation
------------

Add `coverage` as a development dependency:

.. code-block:: console

    uv add --dev coverage

Configuration
-------------

Configure Coverage in your `pyproject.toml`:

.. code-block:: toml

    [tool.coverage.run]
    branch = true
    source = ["src"]

    [tool.coverage.report]
    exclude_lines = [
        "pragma: no cover",
        "def __repr__",
        "if self.debug",
        "raise AssertionError",
        "raise NotImplementedError",
        "if 0:",
        "if __name__ == .__main__.:",
        "fire.Fire",
    ]
    fail_under = 90
    ignore_errors = true
    skip_empty = true

Explanation:

- `branch = true`: Includes branch coverage
- `source`: Directs Coverage to only measure code inside `src/`
- `fail_under = 90`: Fails if total coverage is below 90%
- `exclude_lines`: Skips specific patterns (e.g., debug or entrypoint code)

Usage
-----

Run the test suite with coverage measurement:

.. code-block:: console

    coverage run -m pytest

Generate a terminal summary with line numbers for untested code:

.. code-block:: console

    coverage report -m

Generate a full HTML report:

.. code-block:: console

    coverage html
    brave-browser htmlcov/index.html

This produces an interactive report in `htmlcov/`, where green lines are covered, and red lines are missing test coverage.

Additional Resources
--------------------

- Docs: https://coverage.readthedocs.io/
- Configuration reference: https://coverage.readthedocs.io/en/latest/config.html
- HTML reporting: https://coverage.readthedocs.io/en/latest/cmd.html#html

Next Step
---------

Use **pytest-cov** to integrate Coverage directly into the `pytest` workflow. It simplifies coverage reporting and supports one-step test + coverage execution.

Uninstall
---------

To remove Coverage from your environment:

.. code-block:: console

    uv remove --dev coverage
