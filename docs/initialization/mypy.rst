==================
Type Hinting: MyPy
==================

.. meta::
    :description: Using mypy for static type checking and enforcing type correctness in Python code.

Introduction
------------

Type hinting and checking means providing type references and verifying that values in a program are used in a way consistent with their declared data types. While Python is dynamically typed, tools like `mypy` allow for static type checking without running the code.

Benefits of using type hints with `mypy`:

- Detect type-related bugs early (without executing the program)
- Improve code readability and editor support (e.g., autocompletion)
- Encourage better documentation and long-term maintainability

Key Features
------------

- Static type checking at development time
- Detects type mismatches, missing annotations, and more
- Integrates well with editors and CI pipelines
- Supports type inference, strict checking, and gradual typing

Installation
------------

Install `mypy` using `uv` or `pip`:

.. code-block:: bash

    uv add --dev mypy

Run `mypy` on your source files:

.. code-block:: bash

    mypy src/

Configuration
-------------

To customize behavior, create a `mypy.ini` file in your project root. Here's your current configuration:

.. code-block:: ini

    [mypy]
    python_version = 3.9
    disallow_untyped_defs = true
    ignore_missing_imports = true

- `python_version`: Sets the Python version `mypy` should assume
- `disallow_untyped_defs`: Requires all functions to have type annotations
- `ignore_missing_imports`: Skips errors for third-party modules without stubs

Usage
-----

**Dynamic Typing in Python:**

.. code-block:: python

    x = "hello"  # x is a str
    x = 42       # now x is an int

Python allows this flexibility at runtime, but static checking helps avoid type bugs before deployment.

**Incorrect Type Annotations**

.. code-block:: python

    def add(a, b: int):
        """Add two integers."""
        print("Adding:", a, b)
        res = a + b
        return res

    add(5, "hello")

Run:

.. code-block:: bash

    mypy bad_test.py

Output:

.. code-block:: text

    bad_test.py:4: error: Function is missing a return type annotation  [no-untyped-def]
    bad_test.py:4: error: Function is missing a type annotation for one or more arguments  [no-untyped-def]
    bad_test.py:10: error: Argument 2 to "add" has incompatible type "str"; expected "int"  [arg-type]
    Found 3 errors in 1 file (checked 1 source file)

**Correct Type Annotations**

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

.. code-block:: bash

    mypy good_test.py

Output:

.. code-block:: text

    Success: no issues found in 1 source file

Additional Resources
--------------------

- Mypy Docs: https://mypy.readthedocs.io/en/stable/getting_started.html
- PEP 484 – Type Hints: https://peps.python.org/pep-0484/

Next Step
---------

Once type checking is in place with `mypy`, the next step is to set up **pre-commit** to automatically run tools like `ruff`, `mypy`, and formatters before each commit. This helps enforce consistency and catch issues early in your workflow.

Uninstall
---------

To uninstall `mypy`:

.. code-block:: bash

    uv remove --dev mypy
