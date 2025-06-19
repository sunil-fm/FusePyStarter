==================================
Configuration Management
==================================

Dynaconf
---------

Dynaconf is a powerful and flexible configuration management tool for Python that simplifies how you handle settings and secrets across multiple environments (dev, staging, production, etc.).

It is designed to support:

- Multiple file formats (.toml, .json, .yaml, .env, .ini, etc.)
- Environment switching (dev/staging/prod)
- Layered configuration
    - it loads and merges settings from multiple sources in a prioritized, layered order. Each “layer” can override the values from the previous one — giving you a flexible, environment-aware, and override-friendly configuration setup.
- Built-in secrets management

Why Use Dynaconf?

- It solves common problems like:
- Overriding configs based on environment
- Keeping secrets out of source code
- Loading settings from multiple sources (files, env vars, Redis, Vault, etc.)
- Using default values + overrides cleanly

Code setup
-----------

.. code-block:: python

    from dynaconf import Dynaconf
    
    settings = Dynaconf(
        environments=True,
        envvar_prefix="DYNACONF", 
        load_dotenv = True,
        settings_files=['settings.toml', "secrets/.secrets.toml"], 
    )

environments parameter:
***********************

.. code-block:: python

    environments=True,  # enables [dev], [stage], [prod]

- Have to specify the environment with the below environment variable.

.. code-block:: bash

    export ENV_FOR_DYNACONF=dev
    echo $ENV_FOR_DYNACONF

- Default is loaded always at first whichever the environment is selected.
- Then, if the environment is set, default is loaded and then after the selected environment is loaded.
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
- When `envvar_prefix="DYNACONF"` is set, Dynaconf will look for environment variables that start with `DYNACONF_`.
- Dynaconf accesses os.environ at runtime to override our settings.

.. code-block:: python

    settings = Dynaconf(envvar_prefix="MYAPP") # We can change it as well, if we want a project-specific prefix.

Suppose we have this setting in our settings.toml.

.. code-block:: python

    [default]
    app_name = "MyApp"
    db_url = "sqlite:///local.db"

.. code-block:: bash

    export DYNACONF_DEBUG=true
    export DYNACONF_DB_URL="postgresql://user:pass@host:5432/db"

- Then Dynaconf will override the values from settings.toml using the values from the environment, because the keys match (DEBUG, DB_URL) and are prefixed with `DYNACONF_`.

load_dotenv parameter:
***********************

.. code-block:: python

    load_dotenv = True

- This loads .env into os.environ at runtime, so overrides work like they came from export.
- Otherwise, we would have to `export` to override the environment variable all the time and `.env` wouldn’t work as it wouldn’t load the variable in os.environ. 
