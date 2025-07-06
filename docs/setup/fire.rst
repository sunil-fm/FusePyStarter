============================
Command Line Interface: Fire
============================

Introduction
------------

`Python Fire <https://google.github.io/python-fire/>`_ is a library developed by Google that automatically generates command-line interfaces (CLIs) from Python code. It is especially useful for creating quick utilities, debugging, and exposing modules or scripts as CLI tools with minimal effort.

Key Features
------------

- Turn any Python object (function, class, module, etc.) into a CLI
- No boilerplate or parser setup required
- Useful for both development and production scripts
- Supports argument parsing, help text, and REPL integration
- Easily integrates into Python projects using entry points

Installation
------------

Install Fire using **uv**:

.. code-block:: console

    uv add fire

Configuration
-------------

To use Fire, define a CLI entry point using `fire.Fire()` and configure the CLI command in your `pyproject.toml`.

Define a main function:

.. code-block:: python

    def main():
        fire.Fire(MyCommandClass)

Set up an entry point in `pyproject.toml`:

.. code-block:: toml

    [project.scripts]
    temp-convert = "src.temperature.converter:main"
    advance-convert = "src.temperature.advance_convert:main"

Install the package in editable mode:

.. code-block:: console

    uv pip install -e .

Usage
-----

**Example 1: Function-based CLI**

.. code-block:: python

    from numbers import Real
    import fire

    def celsius_to_fahrenheit(c: Real) -> Real:
        return (c * 9 / 5) + 32

    def main():
        fire.Fire(celsius_to_fahrenheit)

Run it:

.. code-block:: console

    temp-convert 100

**Example 2: Class-based CLI**

.. code-block:: python

    import fire

    class TemperatureConverter:
        @staticmethod
        def convert(temp, from_unit, to_unit):
            valid_units = {"C", "F", "K"}
            if from_unit not in valid_units or to_unit not in valid_units:
                raise ValueError("Invalid temperature unit")
            if from_unit == to_unit:
                return temp
            if from_unit == "C":
                return (temp * 9 / 5) + 32 if to_unit == "F" else temp + 273.15
            elif from_unit == "F":
                return (temp - 32) * 5 / 9 if to_unit == "C" else (temp - 32) * 5 / 9 + 273.15
            elif from_unit == "K":
                return temp - 273.15 if to_unit == "C" else (temp - 273.15) * 9 / 5 + 32

    def main():
        fire.Fire(TemperatureConverter)

Run it:

.. code-block:: console

    advance-convert convert 100 F C

Additional Resources
--------------------

- Official Docs: https://google.github.io/python-fire/
- GitHub Repo: https://github.com/google/python-fire

Next Step
---------

After setting up Python Fire for CLI generation, the next step is to implement **Python Logging** to monitor and trace the behavior of your application.

Uninstall
---------

To remove Fire from your environment:

.. code-block:: console

    uv remove fire
