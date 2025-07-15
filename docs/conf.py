"""Sphinx configuration for building project documentation."""

import os
import sys

import toml

from fusepystarter import __version__

sys.path.insert(0, os.path.abspath("../"))


def _get_project_meta():
    try:
        pyproject_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "pyproject.toml")
        )
        return toml.load(pyproject_path)["project"]
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find pyproject.toml at {pyproject_path}")


pkg_meta = _get_project_meta()
project = pkg_meta["name"]
copyright = "2025, Sunil Ghimire"
author = pkg_meta["authors"][0]["name"]

version = __version__
release = version


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.githubpages",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]


# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"
