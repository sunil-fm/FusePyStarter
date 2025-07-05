=====================
Testing with pytest
=====================

Introduction
------------

**pytest** is a simple yet powerful testing framework for Python. It encourages concise, readable test code and scales to support complex functional testing for applications and libraries. It provides expressive assertions, auto-discovery, and a rich fixture system, making it ideal for both small and large projects.

Key Features
------------

- Rich assert introspection (no need for self.assert* methods)
- Auto-discovery of test files, classes, and functions
- Flexible fixture model for shared test setup and teardown
- Compatible with `unittest` and `nose` test suites
- Thriving plugin ecosystem (e.g., `pytest-cov`, `pytest-mock`)
- Seamless integration with `pre-commit` and CI tools

Installation
------------

Use `uv` to add `pytest` as a development dependency:

.. code-block:: console

    uv add --dev pytest

Configuration
-------------

Configure `pytest` through `pyproject.toml`:

.. code-block:: toml

    [tool.pytest.ini_options]
    testpaths = ["tests"]
    markers = [
        "slow: marks tests as slow",
    ]

This instructs `pytest` to discover tests in the `tests/` directory and register a custom `slow` marker.

Usage
-----

1. Writing Tests
^^^^^^^^^^^^^^^^

.. code-block:: python

    import pytest
    from src.temperature import celsius_to_fahrenheit, fahrenheit_to_celsius

    @pytest.mark.parametrize(
        "celsius, expected_fahrenheit",
        [(0, 32.0), (100, 212.0), (-40, -40.0), (37, 98.6), (25.5, 77.9)],
    )
    def test_celsius_to_fahrenheit(celsius, expected_fahrenheit):
        assert celsius_to_fahrenheit(celsius) == pytest.approx(expected_fahrenheit)

    @pytest.mark.parametrize(
        "fahrenheit, expected_celsius",
        [(32, 0.0), (212, 100.0), (-40, -40.0), (98.6, 37.0), (77.9, 25.5)],
    )
    def test_fahrenheit_to_celsius(fahrenheit, expected_celsius):
        assert fahrenheit_to_celsius(fahrenheit) == pytest.approx(expected_celsius)

2. Fixtures
^^^^^^^^^^^

.. code-block:: python

    @pytest.fixture
    def sample_data():
        return {"name": "Sunil", "age": 30}

    def test_sample_data(sample_data):
        assert sample_data["name"] == "Sunil"

3. Markers
^^^^^^^^^^

Use markers to group or filter tests:

.. code-block:: python

    @pytest.mark.slow
    def test_large_dataset():
        ...

Run only slow tests:

.. code-block:: console

    pytest -m slow

Register custom markers in ``pyproject.toml``:

.. code-block:: toml

    [tool.pytest.ini_options]
    markers = [
        "slow: marks tests as slow",
    ]

4. Common CLI Options
^^^^^^^^^^^^^^^^^^^^^

- `-v`: Verbose mode
- `-q`: Quiet mode
- `-k <expr>`: Filter by name substring
- `-m <marker>`: Run tests with marker
- `--maxfail=<N>`: Stop after N failures
- `--disable-warnings`: Suppress warnings

Example:

.. code-block:: console

    pytest -v -k "fahrenheit" --maxfail=2 --disable-warnings

5. Naming Conventions
^^^^^^^^^^^^^^^^^^^^^

pytest automatically discovers tests that match:

- Files named `test_*.py` or `*_test.py`
- Functions prefixed with `test_`
- Classes prefixed with `Test` (no `__init__` method)

6. Running Tests
^^^^^^^^^^^^^^^^

Run all tests using:

.. code-block:: console

    uv run pytest

7. Integration with pre-commit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Add the following hook to `.pre-commit-config.yaml`:

.. code-block:: yaml

    - repo: local
      hooks:
        - id: test
          name: Run tests
          entry: uv run pytest
          language: python
          args: ["--maxfail=1", "--disable-warnings", "-q"]
          always_run: true
          pass_filenames: false

This ensures that your test suite runs before every commit.

Additional Resources
--------------------

- Pytest documentation: https://docs.pytest.org/
- Awesome Pytest plugins: https://plugincompat.herokuapp.com/
- Parametrization guide: https://docs.pytest.org/en/latest/how-to/parametrize.html

Next Step
---------

Now that testing is set up, the next step is to integrate **test coverage** using the `coverage` tool. This helps ensure your tests are exercising all critical parts of your code.

Uninstall
---------

To remove `pytest`:

.. code-block:: console

    uv remove --dev pytest
