"""Module configuration and version information."""

from configs.config import settings

ENV = settings.get("ENV_FOR_DYNACONF", "dev")

__version__ = "{{cookiecutter.version}}"
