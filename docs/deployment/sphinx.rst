=====================
Sphinx Documentation
=====================

Introduction
------------

**Sphinx** is a powerful tool for generating intelligent and beautiful documentation.
Originally developed for Python's own documentation, Sphinx supports a variety of output formats and is highly extensible.

It is especially well-suited for documenting software projects, including Python-based codebases.
It uses reStructuredText for content markup and integrates tightly with tools like Pygments and Docutils.

Key Features
------------

- **Multiple output formats**: HTML, PDF (via LaTeX), ePub, Texinfo, man pages, plain text, and more.
- **Cross-referencing**: Semantic links for functions, classes, glossary terms, citations, etc.
- **Hierarchical structure**: Easy document tree definition with parent/child navigation.
- **Indexing**: Automatic general and module-specific indices.
- **Syntax highlighting**: Via the Pygments highlighter.
- **Autodoc support**: Pulls docstrings from Python modules automatically.
- **Extensions**: Built-in and third-party extensions, many available via PyPI.

Installation
------------

Install Sphinx as a development dependency using `uv`:

.. code-block:: console

    $ uv add --dev sphinx

Configuration
-------------

Initialize a Sphinx project using:

.. code-block:: console

    $ sphinx-quickstart -v $(uv version | awk '{print $2}') docs

This will generate the following structure:

.. code-block::

    docs
    ├── _build/
    ├── _static/
    ├── _templates/
    ├── conf.py
    ├── index.rst
    ├── make.bat
    └── Makefile

Change the theme to **Read the Docs** for a better look:

.. code-block:: console

    $ uv add --dev sphinx-rtd-theme
    $ uv remove --dev sphinx

Update `conf.py`:

.. code-block:: python

    html_theme = "sphinx_rtd_theme"

Rebuild the docs:

.. code-block:: console

    $ make -C docs clean
    $ make -C docs html
    $ brave-browser docs/_build/html/index.html

Enable autodoc and dynamic metadata in `conf.py`:

.. code-block:: python

    from pathlib import Path
    import toml

    def _get_project_meta():
        project_root = Path(__file__).resolve().parent.parent
        return toml.load(project_root / "pyproject.toml")["project"]

    pkg_meta = _get_project_meta()
    project = pkg_meta["name"]
    copyright = "2025, Sunil Ghimire"
    author = pkg_meta["authors"][0]["name"]
    version = pkg_meta["version"]
    release = version

Enable extensions:

.. code-block:: python

    extensions = [
        "sphinx.ext.autodoc",
        "sphinx.ext.napoleon",
    ]

Usage
-----

Generate documentation from source files:

.. code-block:: console

    $ sphinx-apidoc -o docs/ src

Add the generated modules to `index.rst`:

.. code-block:: rst

    .. toctree::
       :maxdepth: 2
       :caption: Contents:

       modules

Ignore generated `.rst` module files in Git:

.. code-block::

    # Ignore module docs
    src*.rst

Rebuild documentation:

.. code-block:: console

    $ make -C docs clean
    $ make -C docs html
    $ chromium docs/_build/html/index.html

Test documentation build using `tox` by adding this to your `tox.ini`:

.. code-block:: ini

    [tox]
    envlist = ..., docs

    [testenv:docs]
    basepython = python
    changedir = docs
    deps =
        sphinx-rtd-theme
        toml
    commands =
        sphinx-build -b html -d {envtmpdir}/doctrees . {envtmpdir}

Then run:

.. code-block:: console

    $ tox

Additional Resources
--------------------

Useful extensions to consider:

.. code-block:: python

    extensions = [
        "sphinx.ext.autodoc",
        "sphinx.ext.coverage",
        "sphinx.ext.doctest",
        "sphinx.ext.githubpages",
        "sphinx.ext.napoleon",
        "sphinx.ext.todo",
        "sphinx.ext.viewcode",
    ]

To disable `todo` items from appearing in the output:

.. code-block:: python

    todo_include_todos = False

Better syntax highlighting:

.. code-block:: python

    pygments_style = "sphinx"

Next Step
---------

Set up **Continuous Integration** with **GitHub Actions** to automatically test documentation builds.

Uninstall
---------

Remove Sphinx-related packages:

.. code-block:: console

    $ uv remove --dev sphinx-rtd-theme
