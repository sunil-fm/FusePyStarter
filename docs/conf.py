"""Sphinx configuration for building project documentation."""

import os
import sys

sys.path.insert(0, os.path.abspath("../src"))

project = "FusePyStarter"
copyright = "2025, Sunil Ghimire"
author = "Sunil Ghimire"
release = "0.0.1"


extensions = ["sphinx.ext.autodoc", "sphinx.ext.viewcode", "sphinx.ext.napoleon"]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
