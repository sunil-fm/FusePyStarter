
=====================
Testing with pytest
=====================

The **pytest** framework simplifies writing small, readable tests and scales to support
complex functional testing for applications and libraries.

Key Features
------------

- Detailed output for failing assert statements (no need to remember ``self.assert*`` methods)
- Auto-discovery of test modules and functions
- Rich and flexible fixture model for test setup and reuse
- Seamless support for ``unittest`` and ``nose`` test suites
- Compatible with Python 3.5+ and PyPy 3
- Thriving plugin ecosystem (315+ plugins) and active community

For full documentation, visit: https://docs.pytest.org/en/stable/

.. note::

   pytest rewrites assert statements to provide rich introspection output on failure, which makes debugging test failures much easier.

Installation
------------

Use `uv` to add `pytest` as a development dependency:

.. code-block:: console

    $ uv add --dev pytest

Configuration
-------------

Add the following section to your ``pyproject.toml``:

.. code-block:: toml

    [tool.pytest.ini_options]
    testpaths = ["tests"]

This tells pytest to look for tests in the ``tests/`` directory.

Usage Example
-------------

Let's write tests for two simple temperature conversion functions:
``celsius_to_fahrenheit`` and ``fahrenheit_to_celsius``.

.. code-block:: python

    import pytest
    from src.temperature import celsius_to_fahrenheit, fahrenheit_to_celsius

    @pytest.mark.parametrize(
        "celsius, expected_fahrenheit",
        [
            (0, 32.0),       # Freezing point
            (100, 212.0),    # Boiling point
            (-40, -40.0),    # Identical in both scales
            (37, 98.6),      # Human body temperature
            (25.5, 77.9),    # Arbitrary float
        ],
    )
    def test_celsius_to_fahrenheit(celsius, expected_fahrenheit):
        result = celsius_to_fahrenheit(celsius)
        assert result == pytest.approx(expected_fahrenheit)

    @pytest.mark.parametrize(
        "fahrenheit, expected_celsius",
        [
            (32, 0.0),
            (212, 100.0),
            (-40, -40.0),
            (98.6, 37.0),
            (77.9, 25.5),
        ],
    )
    def test_fahrenheit_to_celsius(fahrenheit, expected_celsius):
        result = fahrenheit_to_celsius(fahrenheit)
        assert result == pytest.approx(expected_celsius)

Fixtures
--------

Fixtures are used to manage setup and teardown logic for tests.

.. code-block:: python

    import pytest

    @pytest.fixture
    def sample_data():
        return {"name": "Sunil", "age": 30}

    def test_sample_data(sample_data):
        assert sample_data["name"] == "Sunil"

Markers
-------

pytest allows tests to be grouped or filtered using markers.

.. code-block:: python

    import pytest

    @pytest.mark.slow
    def test_large_dataset():
        # time-consuming test
        ...

To run only tests marked as "slow":

.. code-block:: console

    $ pytest -m slow

To register custom markers in ``pyproject.toml``:

.. code-block:: toml

    [tool.pytest.ini_options]
    markers = [
        "slow: marks tests as slow",
    ]

Common CLI Options
------------------

- ``-v``: Increase verbosity
- ``-q``: Decrease verbosity
- ``-k <expression>``: Run tests matching the expression
- ``-m <marker>``: Run tests matching a marker
- ``--maxfail=<num>``: Stop after N failures
- ``--disable-warnings``: Suppress warnings

Example:

.. code-block:: console

    $ pytest -v -k "fahrenheit" --maxfail=2 --disable-warnings

Naming Conventions
------------------

pytest will automatically discover tests that follow these patterns:

- Files named ``test_*.py`` or ``*_test.py``
- Functions prefixed with ``test_``
- Classes prefixed with ``Test`` (without ``__init__`` methods)

Running Tests
-------------

To run all tests, simply use:

.. code-block:: console

    $ pytest

pytest will automatically discover and run tests matching the naming conventions listed above.

Integration with pre-commit
---------------------------

To run tests automatically before every commit, add the following to your ``.pre-commit-config.yaml``:

.. code-block:: yaml

    - repo: local
      hooks:
        - id: install-dependencies
          name: Install Dependencies
          entry: uv pip install -e .
          language: python
          always_run: true
          pass_filenames: false

        - id: test
          name: Run tests
          entry: uv run pytest
          language: python
          args: ["--maxfail=1", "--disable-warnings", "-q"]
          always_run: true
          pass_filenames: false

This ensures dependencies are installed and tests are executed before every commit, helping catch issues early.

Uninstallation
--------------

To remove pytest:

.. code-block:: console

    $ uv remove --dev pytest

Conclusion
----------

pytest is a powerful, flexible, and widely adopted testing tool that helps you maintain code quality and catch bugs early through simple yet expressive tests.
