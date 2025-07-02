PyFoundry
=========

**A modern Python project forge starting with quality at the core.**

PyFoundry is a work-in-progress Python project template that focuses on doing things right from the start.
This early phase begins with a consistent code style via `.editorconfig`, and will expand to include full tooling for testing, formatting, linting, deployment, and documentation.

📁 Repository Links
-------------------

- 💻 **Source Code**: https://github.com/ghimiresunil/PyFoundry/tree/main
- 🐞 **Issue Tracker**: https://github.com/ghimiresunil/PyFoundry/issues

📂 Contents
-----------

Project Initialization
~~~~~~~~~~~~~~~~~~~~~~

The project is configured with tools that promote consistency and maintainability from the beginning:

- `editorconfig`_ — Ensures consistent indentation, line endings, and formatting across different editors.
- `ruff`_ — Ultra-fast linter and formatter for Python.
- `mypy`_ — Static type checker for Python.
- `pre-commit`_ — Framework for managing and maintaining multi-language pre-commit hooks.

Project Setup
~~~~~~~~~~~~~

The core project setup integrates tools for configuration, CLI handling, testing, and automation:

- `dynaconf`_ — Flexible configuration management.
- `fire`_ — CLI generation from Python code.
- `logging`_ — Built-in logging configuration for visibility and debugging.
- `pytest`_ — Simple yet powerful test framework.
- `coverage`_ — Monitors code coverage during test execution.
- `pytest-cov`_ — Plugin for integrating coverage with pytest.
- `tox`_ — Automates testing across multiple Python environments.

⚙️ Getting Started with `uv`
----------------------------

1. **Clone the repository**

   .. code-block:: bash

      git clone https://github.com/ghimiresunil/PyFoundry.git
      cd PyFoundry

2. **Create a virtual environment**

   .. code-block:: bash

      uv venv .venv
      source .venv/bin/activate

3. **Install project dependencies**

   .. code-block:: bash

      uv sync

🛠️ Coming Soon
--------------

Planned future integrations:

- **Sphinx** — For generating structured project documentation.
- **GitHub Actions** — CI/CD workflows for testing, linting, and deployment.
- **GitHub Pages** — Deploy documentation or project pages directly from the repository.

📬 Contribute or Follow Along
-----------------------------

PyFoundry is evolving. Star the repository, follow development, or contribute by submitting issues and pull requests!

.. _editorconfig: https://github.com/ghimiresunil/PyFoundry/blob/main/docs/initialization/editorconfig.rst
.. _ruff: https://github.com/ghimiresunil/PyFoundry/blob/main/docs/initialization/ruff.rst
.. _mypy: https://github.com/ghimiresunil/PyFoundry/blob/main/docs/initialization/mypy.rst
.. _pre-commit: https://github.com/ghimiresunil/PyFoundry/blob/main/docs/initialization/pre-commit.rst
.. _dynaconf: https://github.com/ghimiresunil/PyFoundry/blob/main/docs/initialization/pre-commit.rst
.. _fire: https://github.com/ghimiresunil/PyFoundry/blob/main/docs/setup/fire.rst
.. _logging: https://github.com/ghimiresunil/PyFoundry/blob/main/docs/setup/logging.rst
.. _pytest: https://github.com/ghimiresunil/PyFoundry/blob/main/docs/setup/pytest.rst
.. _coverage: https://github.com/ghimiresunil/PyFoundry/blob/main/docs/setup/coverage.rst
.. _pytest-cov: https://github.com/ghimiresunil/PyFoundry/blob/main/docs/setup/pytest-cov.rst
.. _tox: https://github.com/ghimiresunil/PyFoundry/blob/main/docs/setup/tox.rst
