"""Singleton logger and execution logging decorator."""

import logging
import threading
from typing import Any, Callable, Optional, TypeVar

from configs.config import settings

T = TypeVar("T", bound=Callable[..., Any])


class AppLogger:
    """Singleton logging class using Dynaconf settings.

    This class configures and provides a singleton logger instance
    that uses settings from a Dynaconf configuration.

    Args:
        logger_name (Optional[str]): Optional name for the logger.

    Attributes:
        _instance (Optional[AppLogger]): The singleton instance of the logger.
        _lock (threading.Lock): A lock to ensure thread-safe instantiation.
        _initialized (bool): Flag indicating if the logger has been initialized.
    """

    _instance: Optional["AppLogger"] = None
    _lock: threading.Lock = threading.Lock()
    _initialized: bool = False

    def __new__(cls, logger_name: Optional[str] = None) -> "AppLogger":
        """Create or return the singleton instance.

        Args:
            logger_name (Optional[str]): Optional name for the logger.

        Returns:
            AppLogger: The singleton logger instance.
        """
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(AppLogger, cls).__new__(cls)
                    cls._instance._initialized = False
        return cls._instance

    def __init__(self, logger_name: Optional[str] = None) -> None:  # noqa: D107
        if self._initialized:
            return
        self._initialized = True

        self.settings = settings
        self.logger_name = logger_name or self.settings.get("app_name", "MyApp")
        self.logger = logging.getLogger(self.logger_name)
        self._configure_logger()

    def _configure_logger(self) -> None:
        """Configure the logger based on settings.

        Returns:
            None: This doesn't return anything meaningful.
        """
        log_level = getattr(logging, self.settings.logging.log_level.upper())
        log_format = self.settings.logging.log_format

        self.logger.handlers.clear()
        self.logger.setLevel(log_level)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)

        formatter = logging.Formatter(log_format)
        console_handler.setFormatter(formatter)

        self.logger.addHandler(console_handler)
        self.logger.propagate = False

    def get_logger(self) -> logging.Logger:
        """Get the configured logger instance.

        Returns:
            logging.Logger: The configured logger.
        """
        return self.logger

    def debug(self, message: str) -> None:
        """Log a debug message.

        Args:
            message (str): The message to log.

        Returns:
            None: This doesn't return anything meaningful.
        """
        self.logger.debug(message)

    def info(self, message: str) -> None:
        """Log an info message.

        Args:
            message (str): The message to log.

        Returns:
            None: This doesn't return anything meaningful.
        """
        self.logger.info(message)

    def warning(self, message: str) -> None:
        """Log a warning message.

        Args:
            message (str): The message to log.

        Returns:
            None: This doesn't return anything meaningful.
        """
        self.logger.warning(message)

    def error(self, message: str) -> None:
        """Log an error message.

        Args:
            message (str): The message to log.

        Returns:
            None: This doesn't return anything meaningful.
        """
        self.logger.error(message)

    def critical(self, message: str) -> None:
        """Log a critical message.

        Args:
            message (str): The message to log.

        Returns:
            None: This doesn't return anything meaningful.
        """
        self.logger.critical(message)
