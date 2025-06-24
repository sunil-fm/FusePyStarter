"""Load configuration using Dynaconf with environment and dotenv support."""

from dynaconf import Dynaconf

settings = Dynaconf(
    environments=True,
    envvar_prefix="DYNACONF",
    load_dotenv=True,
    settings_files=["settings.toml", ".secrets.toml"],
    env_switcher="ENV_FOR_DYNACONF",
)
