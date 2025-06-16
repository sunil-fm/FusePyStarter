============
EditorConfig Configuration
============

.. meta::
   :description: Guidelines for setting up consistent coding styles across editors and IDEs using EditorConfig.

Overview
--------

EditorConfig helps maintain consistent coding styles across different editors and IDEs when multiple developers work on the same project. The system consists of:

- A standardized file format for style definitions
- Editor plugins that interpret these rules

Key Features
~~~~~~~~~~~~
- Version control friendly
- Hierarchical configuration (parent directory inheritance)
- Cross-platform support (Windows/macOS/Linux)

Configuration Discovery
----------------------

When opening a file, EditorConfig:

1. Looks for ``.editorconfig`` in the file's directory
2. Searches parent directories recursively
3. Stops when either:
   - The root directory is reached, or
   - A file containing ``root=true`` is found

.. note:: Windows users should create ``.editorconfig.`` (with trailing dot) which Explorer will rename correctly.

Configuration Rules
-------------------

Create ``.editorconfig`` with these settings:

.. code-block:: ini

    # Top-most configuration file (stops searching parent dirs)
    root = true

    # Default rules for all files
    [*]
    indent_style = space
    indent_size = 4
    end_of_line = lf        # Unix-style
    charset = utf-8         # Universal encoding
    trim_trailing_whitespace = true
    insert_final_newline = true

    # Python-specific rules
    [*.py]
    max_line_length = 88

    # Configuration files
    [*.{json,yml,yaml,toml}]
    indent_size = 2         # Standard for config formats

    # Documentation exceptions
    [*.rst]
    trim_trailing_whitespace = false  # Preserves RST formatting

    # Makefile requirements
    [Makefile]
    indent_style = tab      # Mandatory for makefiles

Implementation Notes
--------------------

1. **Precedence Rules**:
   - Last matching section takes priority
   - Closer files override parent directory settings

2. **Editor Support**:
   - Most modern editors have native support
   - Plugins available for others (see https://editorconfig.org/#download)

Next Steps
----------

.. admonition:: Proceed to Linting Setup

    To configure Python linting:

    .. code-block:: bash

        git stash          # Save current changes
        git checkout init/lint/flake8  # Switch to linting configuration

Additional Resources
--------------------
- Official Documentation: https://editorconfig.org/
- Python Style Guide: https://peps.python.org/pep-0008/
- Black Formatter: https://black.readthedocs.io/

