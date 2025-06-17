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

    # EditorConfig helps developers define and maintain consistent
    # coding styles between different editors and IDEs
    # https://editorconfig.org

    # top-most EditorConfig file
    root = true

    # Unix-style newlines with a newline ending every file
    [*]
    indent_style = space
    indent_size = 4
    end_of_line = lf
    charset = utf-8
    trim_trailing_whitespace = true
    insert_final_newline = false

    # Set default charset
    # 4 space indentation
    [*.py]
    max_line_length = 88

    # Indendation for json, yml, yaml, and toml
    [*.{json,yml,yaml,toml}]
    indent_size = 2

    # Documentation
    [*.rst]
    trim_trailing_whitespace = false

    # Markdown files
    [*.md]
    trim_trailing_whitespace = false

    # Tab indentation (no size specified)
    [Makefile]
    indent_style = tab


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

