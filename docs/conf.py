"""Sphinx configuration for building project documentation."""

import sys
from pathlib import Path

import toml

# -- Path setup --------------------------------------------------------------

# Dynamically determine the project root and src directory
current_dir = Path(__file__).resolve().parent
project_root = current_dir.parent
src_path = project_root / "src"


# Add src to sys.path so packages like `temperature` can be found
sys.path.insert(0, str(src_path))


# -- Project metadata from pyproject.toml ------------------------------------


def _get_project_meta():
    return toml.load(project_root / "pyproject.toml")["project"]


pkg_meta = _get_project_meta()
project = pkg_meta["name"]
copyright = "2025, Sunil Ghimire"
author = pkg_meta["authors"][0]["name"]
version = pkg_meta["version"]
release = version  # Full version


# -- General configuration ---------------------------------------------------

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

# Include TODOs in the output if set to True
todo_include_todos = False

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# Use default syntax highlighting
pygments_style = "sphinx"
