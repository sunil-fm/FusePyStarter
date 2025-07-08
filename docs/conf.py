"""Sphinx configuration for building project documentation."""

import os
import sys
from pathlib import Path

import toml

# Add src directory to Python path for autodoc
sys.path.insert(0, os.path.abspath("../src"))


def _get_project_meta():
    project_root = Path(__file__).resolve().parent.parent
    return toml.load(project_root / "pyproject.toml")["project"]


pkg_meta = _get_project_meta()
project = pkg_meta["name"]
copyright = "2025, Sunil Ghimire"
author = pkg_meta["authors"][0]["name"]

version = pkg_meta["version"]
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
    "sphinx.ext.intersphinx",
]

# Autodoc configuration
autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "special-members": "__init__",
    "undoc-members": True,
    "exclude-members": "__weakref__",
}
autodoc_mock_imports = []  # Add any problematic imports here

# Napoleon settings for Google-style docstrings
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The suffix of source filenames.
source_suffix = [".rst", ".md"]

# The master toctree document.
master_doc = "index"

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# Theme options
html_theme_options = {
    "navigation_depth": 4,
    "collapse_navigation": False,
    "sticky_navigation": True,
    "includehidden": True,
    "titles_only": False,
}

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True

# Output file base name for HTML help builder.
htmlhelp_basename = f"{project}doc"

# -- Options for todo extension ----------------------------------------------
todo_include_todos = False

# -- Options for Pygments ---------------------------------------------------
pygments_style = "sphinx"

# -- Options for intersphinx extension ---------------------------------------
intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}

# -- Options for GitHub Pages -----------------------------------------------
# Ensure links work properly on GitHub Pages
html_baseurl = f"/{project}/"
