Formatter
---------

Formatter is a tool that automatically reformats our code to follow a consistent style of coding enforcing uniformity across codebase. It formats things like:

- Bad spacing, indentation
- Unnecessary parentheses or blank lines
- Consistent quote usage (e.g., always double quotes)
- Import reordering (some formatters like ruff do this)

Examples: black, autopep8, yapf, prettier, go fmt, etc.

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


Incorrect Python Code (Unformatted + Bad Style)
-----------------------------------------------
.. code-block:: python

    import sys,os


    def add( a,b ):
    print("Adding:",a,b)
    return a +  b


    def  subtract(a , b ):
    print( "Subtracting:", a,b )
    return a-b

What is wrong?
--------------

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

Run:
----
.. code-block:: bash

    black bad_code.py


Output After Formatting:
------------------------

.. code-block:: python

    import os
    import sys


    def add(a, b):
        print("Adding:", a, b)
        return a + b


    def subtract(a, b):
        print("Subtracting:", a, b)
        return a - b


What black fixed:
----------------- 

- Cleaned up all spacing around arguments and operators.
- Fixed indentation.
- Reformatted multiple imports into separate lines.
- Standardized quotes, spacing, and returns.
