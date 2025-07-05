============
Type Hinting
============

Type hinting and checking means providing type references and verifying that values in our program are used in a way consistent with their data types. For example, if a function expects a string, type checking ensures you don’t accidentally pass it an integer.

Python is dynamically typed, but `mypy` lets you add static type hints that help:

- Detect type-related errors without running the code.
- Improve code readability and editor support (like autocompletion).
- Enforce better documentation and maintainability.

Types:

- Static
    - Happens before runtime
    - Tools: mypy, pyright, etc
- Dynamic
    - Happens at runtime

Python is dynamically typed.

.. code-block:: bash

    x = "hello"  # x is a str
    x = 42       # now x is an int

Installing mypy
-----------------

.. code-block:: bash

    # Install mypy
    uv add --dev mypy

    # Run mypy on your code
    mypy src/


Incorrect Type Annotations
----------------------------

.. code-block:: python

    def add(a, b: int):
        """Add two integers."""
        print("Adding:", a, b)
        res = a + b
        return res

    add(5, "hello")

Run:
****
.. code-block:: bash

    mypy bad_test.py


Output:
*******
.. code-block:: python

    bad_test.py:4: error: Function is missing a return type annotation  [no-untyped-def]
    bad_test.py:4: error: Function is missing a type annotation for one or more arguments  [no-untyped-def]
    bad_test.py:10: error: Argument 2 to "add" has incompatible type "str"; expected "int"  [arg-type]
    Found 3 errors in 1 file (checked 1 source file)


Correct Type Annotations
----------------------------
Example 1:

.. code-block:: python

    def add(a: int, b: int) -> int:
        """Add two integers."""
        print("Adding:", a, b)
        res = a + b
        return res

    add(5, 6)

Example 2:

.. code-block:: python

    from typing import Any

    def add(a: int, b: int) -> Any:
        """Add two integers."""
        print("Adding:", a, b)
        res = a + b
        final_res = str(res)
        return final_res

    add(5, 6)

Example 3:

.. code-block:: python

    def add(a: int, b: int) -> None:
        """Add two integers."""
        print("Adding:", a, b)
        res = a + b
        print("Result:", res)

    add(5, 6)

Run:
****
.. code-block:: bash

    mypy good_test.py

Output:
*******
.. code-block:: python

    Success: no issues found in 1 source file

Resources
-----------

- https://mypy.readthedocs.io/en/stable/getting_started.html
