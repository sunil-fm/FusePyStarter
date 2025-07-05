============
Testing: tox
============

Introduction
------------

**tox** is a command-line tool that automates testing in isolated environments. It’s primarily used to ensure code works consistently across different Python versions and environments, while simplifying setup and integration with CI/CD pipelines.

tox can run test suites, linters, or any shell command within virtual environments it creates and manages automatically.

Docs: https://tox.readthedocs.io/en/latest/

Key Features
------------

- Automates multi-version Python testing
- Manages isolated test environments with virtualenv
- Integrates seamlessly with `pytest`, `pre-commit`, and linters
- Simplifies CI setup and ensures local-dev parity
- Highly configurable and extensible with plugins

Installation
------------

Install `tox` as a development dependency using `uv`:

.. code-block:: console

    uv add --dev tox

Configuration
-------------

Define environments and commands in a `tox.ini` file at your project root:

.. code-block:: ini

    [tox]
    envlist = py312, py313, pre-commit
    skipsdist = true

    [testenv]
    deps = uv
    allowlist_externals = uv
    commands_pre = uv pip install -e .
    commands = uv run pytest

    [testenv:pre-commit]
    skip_install = true
    deps = pre-commit
    setenv = SKIP=install-dependencies,test
    commands = pre-commit run --all-files

Explanation:

- `envlist`: Environments to run (e.g., Python versions, pre-commit)
- `commands_pre`: Run setup commands like editable install
- `commands`: Run tests with `pytest`
- `skip_install`: Skip package install for environments like `pre-commit`

Usage
-----

Run all defined environments:

.. code-block:: console

    tox

Run a specific environment (e.g., pre-commit only):

.. code-block:: console

    tox -e pre-commit

Run multiple environments:

.. code-block:: console

    tox -e py312,pre-commit

View the full configuration and environment list:

.. code-block:: console

    tox -av

Additional Resources
--------------------

- Official Docs: https://tox.readthedocs.io/
- GitHub: https://github.com/tox-dev/tox
- tox plugins: https://tox.readthedocs.io/en/latest/plugins.html

Next Step
---------

Set up **Sphinx** for generating clean, versioned project documentation. Sphinx is highly extensible and integrates with `reStructuredText`, `Markdown`, and docstring introspection.

Uninstall
---------

To remove tox:

.. code-block:: console

    uv remove --dev tox
