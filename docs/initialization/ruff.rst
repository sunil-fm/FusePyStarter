====================
Linter and Formatter
====================

.. meta::
    :description: Tools to enforce the uniformity in coding following the best practices

Linter
------

Linter is a tool that analyses our source code to find problems and help enforce code quality and best practices by detecting issues before runtime. It finds problems such as:

- Syntax errors
- Style guide violations
- Unused variables/imports
- Possible bugs or logical issues

Examples of Linters: flake8, ruff, pylint, estline (JavaScript/TypeScript), golint (Go), etc

Incorrect Python Code (Unformatted + Bad Style)
*************************************************
.. code-block:: python

    import sys,os


    def add( a,b ):
    print("Adding:",a,b)
    return a +  b


    def  subtract(a , b ):
    print( "Subtracting:", a,b )
    return a-b

What is wrong?
**************

- Formatting:
    - Inconsistent indentation
    - Extra spaces around parameters
    - Bad spacing in return statement

- Import style:
    - import sys, os violates PEP8 (imports should be separate lines)

- Indentation:
    - print in add() is poorly indented

- Function spacing:
    - Extra spaces around function names and arguments

- Output formatting:
    - Spaces inside print values are inconsistent

Installing the Package:
***********************

.. code-block:: bash

    uv add --dev ruff

Run:
****
.. code-block:: bash

    ruff check bad_code.py

Output:
*******
.. code-block:: bash

    F401: 'sys' imported but unused
    E401: Multiple imports on one line
    
Note: to get the detailed check, you can use flake8.

.. code-block:: bash

    E231: Missing whitespace after ',' '('
    E271 multiple spaces after keyword, operator


Formatter
---------

Formatter is a tool that automatically reformats our code to follow a consistent style of coding enforcing uniformity across codebase. It formats things like:

- Bad spacing, indentation
- Unnecessary parentheses or blank lines
- Consistent quote usage (e.g., always double quotes)
- Import reordering (some formatters like ruff do this)

Examples: black, ruff, autopep8, yapf, prettier, go fmt, etc.

*Note:* Formatters will not fix all the issues captured by linters.

Formatters do not detect or fix:

- Unused variables
- Incorrect logic
- Wrong function arguments
- Undefined variables
- Unreachable code
- Bad naming conventions
- Missing docstrings or type hints

These are logic or semantic issues and require linters and type checkers (mypy).

Run:
****
.. code-block:: bash

    ruff format bad_code.py


Output After Formatting:
************************

.. code-block:: python

    import sys, os


    def add(a, b):
        print("Adding:", a, b)
        return a + b


    def subtract(a, b):
        print("Subtracting:", a, b)
        return a - b


What ruff fixed:
*****************

- Cleaned up all spacing around arguments and operators.
- Fixed indentation.
- Standardized quotes, spacing, and returns.


Ruff fixing issues
-------------------

if we want ruff to automatically fix issues:

.. code-block:: bash
    
    ruff check bad_code.py --fix


Output After Formatting:
************************

.. code-block:: python


    def add(a, b):
        print("Adding:", a, b)
        return a + b


    def subtract(a, b):
        print("Subtracting:", a, b)
        return a - b


What ruff fixed:
****************

- Unnecessary imports also got removed



Ruff Usage in a Project
--------------

Run the below commands as per the need to check, fix or format the code.

.. code-block:: bash

    # Check for issues
    ruff check bad_code.py      # Check a specific file for issues
    ruff check .                # Check all files in the current directory

    # Format the code
    ruff format bad_code.py

    # Fix issues automatically
    ruff check bad_code.py --fix

    # Run all checks and fixes
    ruff check bad_code.py --fix --select E,F

Resources:
----------

- https://docs.astral.sh/ruff/
- https://peps.python.org/pep-0008/
