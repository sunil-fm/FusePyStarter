============
Linters
============

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
Formatting:
- Inconsistent indentation
- Extra spaces around parameters
- Bad spacing in return statement

Import style:
- import sys, os violates PEP8 (imports should be separate lines)

Indentation:
- print in add() is poorly indented

Function spacing:
- Extra spaces around function names and arguments

Output formatting:
- Spaces inside print values are inconsistent

Run:
----
.. code-block:: bash
    ruff bad_code.py

Output:
-------
.. code-block:: bash
    F401: 'sys' imported but unused
    E231: Missing whitespace after ','
    E701: Multiple statements on one line (colon)
    E302: Expected 2 blank lines, found 1
