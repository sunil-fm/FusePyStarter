==========================
EditorConfig Configuration
==========================

.. meta::
   :description: Guidelines for setting up consistent coding styles across editors and IDEs using EditorConfig.

Introduction
------------

EditorConfig helps maintain consistent coding styles across different editors and IDEs when multiple developers work on the same project. The system consists of:

- A standardized file format for style definitions
- Editor plugins that interpret these rules

Key Features
~~~~~~~~~~~~
- Version control friendly
- Hierarchical configuration (parent directory inheritance)
- Cross-platform support (Windows/macOS/Linux)

Installation
------------

To enable EditorConfig support:

1. Check if your code editor has native support (most modern editors do).
2. If not, install the appropriate plugin: https://editorconfig.org/#download

.. note::
   Windows users should create ``.editorconfig.`` (with trailing dot), which Explorer will rename correctly.

Configuration
-------------

EditorConfig discovers its configuration by:

1. Looking for ``.editorconfig`` in the file's directory
2. Searching parent directories recursively
3. Stopping when:
   - The root directory is reached, or
   - A file containing ``root=true`` is found

Create a ``.editorconfig`` file with the following settings:

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

    # Indentation for json, yml, yaml, and toml
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

Usage
-----

**Precedence Rules**:
- Last matching section takes priority
- Files closer to the target override more distant configurations

**Supported Editors**:
- Most popular editors (VS Code, Atom, Sublime Text, etc.) have built-in or plugin-based support

For installation instructions per editor, refer to the [official EditorConfig downloads page](https://editorconfig.org/#download).

Additional Resources
--------------------

- Official Documentation: https://editorconfig.org/
- Python Style Guide (PEP8): https://peps.python.org/pep-0008/
- Black Formatter: https://black.readthedocs.io/

Next Step
---------
After setting up `.editorconfig`, the next step is to configure **Ruff** — a fast Python linter and formatter. Ruff enforces consistent code style, catches common errors, and integrates rules from tools like Flake8, isort, and Black.

It ensures your Python code remains clean, readable, and compliant with modern best practices.

Uninstall
---------

To disable EditorConfig:

- Remove or rename the ``.editorconfig`` file
- Disable or uninstall the plugin from your code editor (if applicable)
