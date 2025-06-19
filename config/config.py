import os
from dynaconf import Dynaconf

settings = Dynaconf(
    environments=True,  # enables [dev], [stage], [prod]
    envvar_prefix="DYNACONF", # sets the prefix for overriding values with environment variables (via export)
    load_dotenv = True, # loads .env file if exists
    settings_files=['settings.toml', "secrets/.secrets.toml"], # supports any order (the later files can override earlier ones).
)

# , f'secrets/.secrets.{os.getenv("ENV_FOR_DYNACONF")}.toml'