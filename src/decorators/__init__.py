"""Initialize decorators package and expose public logging utilities."""

from src.decorators.logging_service import AppLogger

app_logger = AppLogger()
logger = app_logger.get_logger()

__all__ = ["logger"]
