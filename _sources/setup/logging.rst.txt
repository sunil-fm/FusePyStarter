================
Python Logging
================

Introduction
------------

Python’s built-in `logging` module provides a flexible framework for emitting log messages from Python programs. Logging is essential for monitoring, debugging, and auditing your application without relying on `print()` statements. This setup uses a singleton logger pattern with environment-specific configuration via `Dynaconf`, and includes a decorator for tracing function execution.

Key Features
------------

- Uses **Python standard logging** (no external logging libraries)
- Singleton logger pattern to avoid duplicated log handlers
- Environment-aware configuration using **Dynaconf**
- Supports runtime log level switching (e.g., DEBUG in dev, WARNING in prod)
- Includes a `log_execution` decorator for:
  - Function entry and exit tracing
  - Argument and return value logging
  - Exception logging
  - Execution time measurement

Installation
------------

Make sure `dynaconf` is already install to manage logging configurations:

.. code-block:: bash

    uv add dynaconf

Configuration
-------------

Define logging settings using `Dynaconf`, e.g., in `settings.toml`:

.. code-block:: toml

    [default]
    log_format = "[{levelname}] {asctime} - {message}"
    log_datefmt = "%Y-%m-%d %H:%M:%S"

    [dev]
    log_level = "DEBUG"

    [stage]
    log_level = "INFO"

    [prod]
    log_level = "WARNING"

Set the environment variable to control which config is loaded:

.. code-block:: bash

    export ENV_FOR_DYNACONF=development

Usage
-----

Import and use the logger across modules:

.. code-block:: python

    from src.decorators import logger, log_execution

    @log_execution
    def calculate_area(length, width):
        return length * width

    logger.info("Started area calculation")

Example output:

.. code-block:: text

    INFO     Entering: calculate_area
    DEBUG    Args: (5, 3), kwargs: {}
    INFO     calculate_area completed in 0.0001s
    DEBUG    Return: 15

To get the logger instance anywhere:

.. code-block:: python

    from src.decorators import logger

    logger.warning("Something might be wrong")

Additional Resources
--------------------

- Python Logging Docs: https://docs.python.org/3/library/logging.html

Next Step
---------

Now that logging is in place, the next step is to integrate **pytest** — a simple yet powerful testing framework for writing unit, functional, and integration tests.

Uninstall
---------

If you wish to remove logging-related configuration:

.. code-block:: bash

    uv remove dynaconf
