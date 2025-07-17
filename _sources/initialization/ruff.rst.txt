====================
Linter and Formatter: Ruff
====================

.. meta::
    :description: Tools to enforce the uniformity in coding following the best practices

Introduction
------------

Ruff is an extremely fast Python linter and formatter that helps maintain consistent code quality by detecting syntax issues, enforcing style guidelines, and fixing common formatting problems. It supports rules from Flake8, Black, isort, pydocstyle, and others.

Key Features
------------

- Lightning-fast performance
- Built-in support for linting and formatting
- Compatible with popular linting standards (PEP8, Flake8, etc.)
- Highly configurable with `ruff.toml`
- Supports automatic fixes
- Compatible with multiple Python versions

Installation
------------

Use `uv` or `pip` to install Ruff as a development dependency:

.. code-block:: bash

    uv add --dev ruff


Configuration
-------------

Create a `ruff.toml` at the root of your project with the following content:

.. code-block:: toml

    show-fixes = true
    target-version = "py312"

    [lint]
    select = ["E", "F", "D"]
    ignore = ["D212"]
    extend-select = []
    pydocstyle.convention = "google"

    [format]
    quote-style = "double"
    indent-style = "space"
    skip-magic-trailing-comma = true
    line-ending = "lf"

Usage
-----

**1. Incorrect Python Code (Unformatted + Bad Style):**

.. code-block:: python

    import sys,os


    def add( a,b ):
    print("Adding:",a,b)
    return a +  b


    def  subtract(a , b ):
    print( "Subtracting:", a,b )
    return a-b

**What is wrong?**

- Inconsistent indentation and spacing
- Multiple imports on one line
- Poor formatting inside `print` statements
- Violates PEP8 style guide

**2. Run Ruff to Lint the Code**

.. code-block:: bash

    ruff check bad_code.py

**Example Output:**

.. code-block:: bash

    F401: 'sys' imported but unused
    E401: Multiple imports on one line
    E231: Missing whitespace after ','
    E271: Multiple spaces after keyword, operator

**3. Run Ruff to Format the Code**

.. code-block:: bash

    ruff format bad_code.py

**Output After Formatting:**

.. code-block:: python

    import sys, os


    def add(a, b):
        print("Adding:", a, b)
        return a + b


    def subtract(a, b):
        print("Subtracting:", a, b)
        return a - b

**What Ruff Fixed:**

- Cleaned up spacing and indentation
- Standardized function signatures
- Normalized print formatting

**4. Auto-fix Issues**

To fix both formatting and linting issues:

.. code-block:: bash

    ruff check bad_code.py --fix

**Output After Auto-fix:**

.. code-block:: python

    def add(a, b):
        print("Adding:", a, b)
        return a + b


    def subtract(a, b):
        print("Subtracting:", a, b)
        return a - b

**What Ruff Fixed:**

- Removed unused imports
- Auto-corrected formatting and spacing issues

**5. Ruff Usage in a Project**

.. code-block:: bash

    # Check for issues
    ruff check bad_code.py
    ruff check .

    # Format code
    ruff format bad_code.py

    # Fix lint errors automatically
    ruff check bad_code.py --fix

    # Run all checks and fixes selectively
    ruff check bad_code.py --fix --select E,F

Additional Resources
--------------------

- Ruff documentation: https://docs.astral.sh/ruff/
- PEP8 style guide: https://peps.python.org/pep-0008/

Next Step
---------

Once Ruff is configured, the next step is to integrate **mypy** for static type checking. While Ruff enforces style and catches common bugs, mypy ensures that your code complies with Python's type hints and helps catch type-related errors before runtime.

Uninstall
---------

To remove Ruff from your project:

.. code-block:: bash

    uv remove --dev ruff
