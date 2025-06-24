
============
Dynaconf
============

Dynaconf is a powerful and flexible configuration management tool for Python that simplifies how you handle settings and secrets across multiple environments (dev, staging, production, etc.).
Why Use Dynaconf?
-----------------

It solves common problems like:

- Overriding configs based on environment
- Keeping secrets out of source code
- Loading settings from multiple sources (files, env vars, Redis, Vault, etc.)
- Using default values + overrides cleanly

Features
--------

* Inspired by the `12-factor application guide`_
* **Settings management** (default values, validation, parsing, templating)
* Protection of **sensitive information** (passwords/tokens)
* Multiple **file formats** ``toml|yaml|json|ini|py`` and also customizable loaders.
* Full support for **environment variables** to override existing settings (dotenv
  support included).
* Optional layered system for **multi environments** ``[default, development, testing,
  production]`` (also called multi profiles)
* Built-in support for **Hashicorp Vault** and **Redis** as settings and secrets
  storage.
* Built-in extensions for **Django** and **Flask** web frameworks.
* **CLI** for common operations such as ``init, list, write, validate, export``.
* Layered configuration
    * it loads and merges settings from multiple sources in a prioritized, layered order. Each “layer” can override the values from the previous one — giving you a flexible, environment-aware, and override-friendly configuration setup.

Installation
------------

.. code-block:: bash

    uv add dynaconf

Code setup
----------

.. code-block:: python

    from dynaconf import Dynaconf

    settings = Dynaconf(
        environments=True,
        envvar_prefix="DYNACONF",
        load_dotenv=True,
        settings_files=['settings.toml', "secrets/.secrets.toml"],
    )

environments parameter:
***********************

.. code-block:: python

    environments=True  # enables [dev], [stage], [prod]

- You have to specify the environment with the below environment variable.

.. code-block:: bash

    export ENV_FOR_DYNACONF=dev
    echo $ENV_FOR_DYNACONF

- Default is loaded always first, whichever the environment is selected.
- Then, if the environment is set, default is loaded and then the selected environment is loaded.
- If export ENV_FOR_DYNACONF=prod, then Dynaconf will load [default] and then override with [prod].

settings_files parameter:
*************************

.. code-block:: python

    settings_files=['settings.toml', "secrets/.secrets.toml"]

- The settings_files argument tells Dynaconf which configuration files to load, in order of priority.
- Values in .secrets.toml will override values in settings.toml if keys conflict.
- If we set ENV_FOR_DYNACONF=prod, Dynaconf will look for:
    - [default] section in both files
    - [prod] section in both files

envvar_prefix parameter:
*************************

- It defines a prefix that Dynaconf uses when looking up environment variables to override your settings.
- When envvar_prefix="DYNACONF" is set, Dynaconf will look for environment variables that start with DYNACONF_.
- Dynaconf accesses os.environ at runtime to override our settings.

.. code-block:: python

    settings = Dynaconf(envvar_prefix="MYAPP")  # We can change it as well, if we want a project-specific prefix.

Suppose we have this setting in our settings.toml.

.. code-block:: toml

    [default]
    app_name = "MyApp"
    db_url = "sqlite:///local.db"

.. code-block:: bash

    export DYNACONF_DEBUG=true
    export DYNACONF_DB_URL="postgresql://user:pass@host:5432/db"

- Then Dynaconf will override the values from settings.toml using the values from the environment, because the keys match (DEBUG, DB_URL) and are prefixed with DYNACONF_.

load_dotenv parameter:
***********************

.. code-block:: python

    load_dotenv = True

- This loads .env into os.environ at runtime, so overrides work like they came from export.
- Otherwise, we would have to export to override the environment variable all the time and .env wouldn’t work as it wouldn’t load the variable in os.environ.

Unset environment variables
---------------------------

.. code-block:: bash

    unset ENV_FOR_DYNACONF
    unset DYNACONF_DB_URL

Advanced Features
-----------------

- Switch Work Environment
- CLI

Update entry point scripts

.. code-block:: toml

    [project.scripts]
    temp-convert = "src.temperature._cli:main"

Install package

.. code-block:: bash

    uv pip install -e .

Run command

.. code-block:: bash

    temp-convert advance_temp convert 100 F C

Switch between environments

- **from_env**: Creates a new settings instance pointing to defined env. Useful for accessing a limited number of config variables at once.
- **setenv** (not recommended): Sets the existing instance to defined env. May cause issues since it's not global.
- **using_env**: Context manager for temporary environment switch.


Examples: Switching Environments in Code
----------------------------------------

- **from_env (Recommended)**

Creates a **new settings instance** for the specified environment.

.. code-block:: python

    from dynaconf import settings

    # Create a new settings instance from 'prod'
    prod_settings = settings.from_env("prod")

    print(prod_settings.db_url)      # Outputs: postgresql://prod_user:prod_pass@prod_host:5432/prod_db
    print(prod_settings.app_name)    # Outputs: MyApp

- **setenv (Not Recommended)**

**Mutates the global settings instance** — use with caution.

.. code-block:: python

    from dynaconf import settings

    # Switch the current settings instance to 'prod'
    settings.setenv("prod")

    print(settings.db_url)  # Outputs: postgresql://prod_user:prod_pass@prod_host:5432/prod_db

- **using_env (Context Manager — Recommended)**

Temporarily switches the environment for a block of code.

.. code-block:: python

    from dynaconf import settings

    print(settings.db_url)  # Outputs: sqlite:///local.db (default)

    with settings.using_env("prod"):
        print(settings.db_url)  # Outputs: postgresql://prod_user:prod_pass@prod_host:5432/prod_db

    # Back to original env
    print(settings.db_url)  # Outputs: sqlite:///local.db


Uninstall
---------

.. code-block:: console

    $ uv remove dynaconf

Other features
--------------

* Secrets_
* Merging_
* `Dynamic Variables`_
* CLI_
* Validation_
* Flask_
* Django_
* `Advanced usage`_

.. _12-factor application guide: https://12factor.net/config
.. _Secrets: https://www.dynaconf.com/secrets/
.. _Merging: https://www.dynaconf.com/merging/
.. _Dynamic Variables: https://www.dynaconf.com/dynamic/
.. _CLI: https://www.dynaconf.com/cli/
.. _Validation: https://www.dynaconf.com/validation/
.. _Flask: https://www.dynaconf.com/flask/
.. _Django: https://www.dynaconf.com/django/
.. _Advanced usage: https://www.dynaconf.com/advanced/
