
============================
Command Line Interface: Fire
============================

`Python Fire <https://google.github.io/python-fire/>`_ is a library for automatically generating command-line interfaces (CLIs) from any Python object.

Overview
--------

- Python Fire is a simple way to create a CLI in Python.
- It is a helpful tool for developing and debugging Python code.
- It helps with exploring existing code or turning other people's code into a CLI.
- Python Fire makes transitioning between Bash and Python easier.
- It also improves the Python REPL experience by preloading modules and variables.

Installation
------------

To install Fire using **uv**:

.. code-block:: console

    uv add fire

Basic Usage
-----------

You can call ``fire.Fire()`` on any Python object—functions, classes, modules, dictionaries, etc.

Example: Function-based CLI

.. code-block:: python

    from numbers import Real
    import fire

    def celsius_to_fahrenheit(c: Real) -> Real:
        """Convert Celsius to Fahrenheit

        Args:
            c (Real): Temperature in Celsius

        Returns:
            Real: Temperature in Fahrenheit
        """
        return (c * 9 / 5) + 32

    if __name__ == "__main__":
        fire.Fire(celsius_to_fahrenheit)

Usage from the command line:

.. code-block:: console

    uv run -m src.temperature.converter 100

Example: Class-based CLI
------------------------

.. code-block:: python

    import fire

    class TemperatureConverter:
        @staticmethod
        def convert(temp, from_unit, to_unit):
            """Convert between temperature units with validation"""
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

    if __name__ == "__main__":
        fire.Fire(TemperatureConverter)

Run from the command line:

.. code-block:: console

    uv run -m src.temperature.advanced convert 100 F C

Self-defined Commands with Entry Points
---------------------------------------

To simplify CLI commands, define a ``main`` function instead of using ``if __name__ == "__main__"``:

Before:

.. code-block:: python

    if __name__ == "__main__":
        fire.Fire(TemperatureConverter)

After:

.. code-block:: python

    def main():
        fire.Fire(TemperatureConverter)

Then register the entry point in ``pyproject.toml`` under ``[project.scripts]``:

.. code-block:: toml

    [project.scripts]
    temp-convert = "src.temperature.converter:main"
    advance-convert = "src.temperature.advance_convert:main"

Install your package in editable mode:

.. code-block:: console

    uv pip install -e .

Now you can run the CLI commands directly:

.. code-block:: console

    temp-convert 100

    advance-convert convert 100 F C

Uninstall
---------

To uninstall the Fire library:

.. code-block:: console

    uv remove fire
