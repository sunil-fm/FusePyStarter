========
Dynaconf
========

Introduction
------------

Dynaconf is a powerful and flexible configuration management tool for Python that simplifies how you handle settings and secrets across multiple environments (dev, staging, production, etc.).

Key Features
------------

- Inspired by the `12-factor application guide`_
- Settings management with defaults, validation, parsing, and templating
- Protection of sensitive information like passwords and tokens
- Supports multiple file formats: ``toml``, ``yaml``, ``json``, ``ini``, ``py``
- Environment variable overrides with dotenv support
- Layered configuration for multi environments: ``default``, ``development``, ``testing``, ``production``
- Built-in support for Hashicorp Vault and Redis for secrets management
- Extensions for Django and Flask web frameworks
- CLI for operations like ``init``, ``list``, ``write``, ``validate``, and ``export``
- Layered merging of settings from prioritized sources

Installation
------------

.. code-block:: bash

    uv add dynaconf

Configuration
-------------

Use Dynaconf in your Python code:

.. code-block:: python

    from dynaconf import Dynaconf

    settings = Dynaconf(
        environments=True,
        envvar_prefix="DYNACONF",
        load_dotenv=True,
        settings_files=['settings.toml', "secrets/.secrets.toml"],
    )

- `environments=True` enables environment sections like `[dev]`, `[prod]`
- `envvar_prefix="DYNACONF"` prefixes environment variables for overrides
- `load_dotenv=True` loads variables from a `.env` file
- `settings_files` is a prioritized list of config files loaded by Dynaconf

Usage
-----

- Select environment by setting:

  .. code-block:: bash

      export ENV_FOR_DYNACONF=dev

- Access settings in code:

  .. code-block:: python

      print(settings.app_name)
      print(settings.db_url)

- Switch environments in code:

  - Create new instance for environment (recommended):

    .. code-block:: python

        prod_settings = settings.from_env("prod")
        print(prod_settings.db_url)

  - Temporary context switch:

    .. code-block:: python

        with settings.using_env("prod"):
            print(settings.db_url)

Additional Resources
--------------------

- Dynaconf Official Docs: https://www.dynaconf.com/
- Secrets Management: https://www.dynaconf.com/secrets/
- Advanced Usage: https://www.dynaconf.com/advanced/
- 12-factor Config Guide: https://12factor.net/config

Next Step
---------

After setting up Dynaconf, the next step is to explore **Fire**, a CLI generation tool that turns Python code into command-line interfaces easily.

Uninstall
---------

.. code-block:: bash

    uv remove dynaconf


.. _12-factor application guide: https://12factor.net/config
