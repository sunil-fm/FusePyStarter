
PyFoundry
=========

**A modern Python project forge starting with quality at the core.**

PyFoundry is a work-in-progress Python project template that focuses on doing things right from the start.  
This early stage begins with consistent code style using `.editorconfig`, with plans to integrate full tooling for testing, formatting, linting, and deployment.

📁 Repository Links
-------------------

- 💻 **Source Code**: https://github.com/ghimiresunil/PyFoundry/tree/main  
- 🐞 **Issue Tracker**: https://github.com/ghimiresunil/PyFoundry/issues

📂 Contents
-----------

Project Initialization
~~~~~~~~~~~~~~~~~~~~~~

- `editorconfig`_ — Ensures consistent indentation, line endings, and formatting across all editors.

⚙️ Getting Started with `uv`
----------------------------

1. Clone the repository:

   .. code-block:: bash

      git clone https://github.com/ghimiresunil/PyFoundry.git
      cd PyFoundry

2. Create a virtual environment:

   .. code-block:: bash

      uv venv .venv
      source .venv/bin/activate

3. Sync dependencies:

   .. code-block:: bash

      uv sync

4. Run tests (if `pytest` is installed in `pyproject.toml`):

   .. code-block:: bash

      uv run pytest

If `pytest` is not set up yet, you can install it temporarily with:

.. code-block:: bash

   uv add --dev pytest

🛠️ Coming Soon
--------------

- Pre-commit hooks with `flake8`, `ruff`, `mypy` and `.pre-commit`
- Automated testing setup using `pytest`, `tox`, and `coverage`
- Documentation with `Sphinx`
- GitHub Actions for CI/CD
- PyPI deployment via `pyproject.toml`

📬 Contribute or Follow Along
-----------------------------

PyFoundry is evolving. Star the repo, follow along, or open an issue if you'd like to contribute!

.. _editorconfig: https://github.com/ghimiresunil/PyFoundry/blob/main/docs/initialization/editorconfig.rst
