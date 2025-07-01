=======================
Testing: Coverage (CLI)
=======================

**Coverage.py** is a tool for measuring code coverage of Python programs. It tracks
which parts of your code have been executed and identifies untested areas. This helps
you assess test effectiveness and improve test completeness.

For more information, visit the `official docs <https://coverage.readthedocs.io/>`_.

Installation
============

Install Coverage as a development dependency using `uv`:

.. code-block:: console

    $ uv add --dev coverage

Configuration
=============

Coverage can be configured directly in ``pyproject.toml``:

.. code-block:: toml

    [tool.coverage.run]
    branch = true
    source = ["src"]

    [tool.coverage.report]
    # Regexes for lines to exclude from consideration
    exclude_lines = [
        "pragma: no cover",              # manual exclusion
        "def __repr__",                  # debug representation
        "if self.debug",                 # debug-only conditions
        "raise AssertionError",          # defensive assertions
        "raise NotImplementedError",     # placeholders
        "if 0:",                         # dead code
        "if __name__ == .__main__.:",    # script entrypoint
        "fire.Fire",                     # fire CLI commands
    ]
    fail_under = 90                     # fail if coverage is below 90%
    ignore_errors = true                # skip errors in unreachable files
    skip_empty = true                   # ignore files with no executable code

Usage
=====

Run the test suite with coverage enabled:

.. code-block:: console

    $ coverage run -m pytest

Generate a terminal summary with missing line numbers:

.. code-block:: console

    $ coverage report -m

Generate a detailed HTML report:

.. code-block:: console

    $ coverage html
    $ brave-browser htmlcov/index.html

The HTML report will be saved in the ``htmlcov/`` directory and gives a visual breakdown
of tested and untested lines.

Uninstallation
==============

To remove Coverage from the development environment:

.. code-block:: console

    $ uv remove --dev coverage
