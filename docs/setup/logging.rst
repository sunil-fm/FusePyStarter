================
Python Logging
================

A structured and reusable logging utility for Python applications, built using a singleton pattern and enriched with an execution logging decorator.

Why Logging?
============

Logging is critical for understanding, debugging, and monitoring applications in development and production. It enables you to:

- Record important runtime events and application state
- Track errors and diagnose issues
- Measure performance metrics (e.g., execution time)
- Enable observability without altering control flow
- Provide audit trails for sensitive operations

Overview
========

This module includes two core utilities:

- ``AppLogger``: A singleton-based logger using Dynaconf configuration, with thread-safe instantiation and configurable log level/format.
- ``log_execution``: A decorator that logs detailed runtime metadata for functions or methods, such as arguments, execution time, return value, and exceptions.

Key Concepts
============

Singleton Logger
----------------

Only one logger instance is created and reused across the application. This avoids:

- Duplicate log entries
- Re-attached handlers
- Inconsistent configurations

Dynaconf Integration
--------------------

The logger is configured using `Dynaconf` settings (e.g., log level and format), allowing environment-specific configurations.

Environment-Based Logging Levels
--------------------------------

Define log levels per environment to reduce noise and improve focus:

- **Development**: ``DEBUG`` (all messages; helpful for debugging)
- **Staging**: ``INFO`` (key application flow and test validation logs)
- **Production**: ``WARNING`` and above (essential alerts and failures only)

Execution Logging Decorator
---------------------------

The `log_execution` decorator:

- Logs method/function entry and exit
- Logs positional and keyword arguments
- Measures and logs execution time
- Captures and logs exceptions and stack traces

Usage
=====

.. code-block:: python

    from src.decorators import logger, log_execution

    @log_execution
    def calculate_area(length, width):
        return length * width

    logger.info("Started computation")

Output example:

.. code-block:: text

    INFO     Entering: calculate_area
    DEBUG    Args: (5, 3), kwargs: {}
    INFO     calculate_area completed in 0.0001s
    DEBUG    Return: 15

AppLogger Class
===============

.. autoclass:: src.decorators.AppLogger
   :members:
   :undoc-members:
   :show-inheritance:

log_execution Decorator
=======================

.. autofunction:: src.decorators.log_execution
    :no-index:

Comparison: Python Logging vs. Loguru
=====================================

.. list-table::
   :widths: 25 35 40
   :header-rows: 1

   * - Feature
     - Python Standard Logging
     - Loguru
   * - Configuration
     - Verbose and boilerplate-heavy
     - Simple, no configuration needed
   * - Flexibility
     - Highly customizable (handlers, filters, formatters)
     - Batteries-included; automatic context logging
   * - Performance
     - Fine-tuned, low-level control
     - More overhead due to rich features
   * - Typing and IDE Support
     - Fully typed, static analysis friendly
     - Less typing, more magic
   * - Integration
     - Easily integrates into existing enterprise apps
     - Better suited for new projects and scripts
   * - Decorator Support
     - Requires manual implementation
     - Built-in with `logger.catch` and decorators

Logging Best Practices
======================

- Use centralized logging settings (e.g., Dynaconf)
- Match log levels to environment (Debug in Dev, Info in Stage, Warning in Prod)
- Use `INFO` for app flow and operational events
- Use `DEBUG` for internal diagnostics and verbose output
- Use `WARNING`, `ERROR`, and `CRITICAL` for failure levels
- Avoid using `print()` for production logging
- Never log sensitive data (e.g., credentials, PII)
- Use exception logging (`logger.exception()` or `log_execution`) for error traces
- Keep logs structured and consistent for future parsing

Package Initialization
======================

The `src.decorators.__init__.py` exposes logging utilities for convenient imports:

.. code-block:: python

    from src.decorators.logging_service import AppLogger, log_execution

    app_logger = AppLogger()
    logger = app_logger.get_logger()

    __all__ = ["logger", "log_execution"]
