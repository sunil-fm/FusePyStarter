"""Temperature conversion functions between Celsius and Fahrenheit."""

from src.decorators import log_execution


@log_execution
def celsius_to_fahrenheit(c: float) -> float:
    """Convert Celsius to Fahrenheit.

    Args:
        c (float): Temperature in Celsius

    Returns:
        float: Temperature in Fahrenheit
    """
    return (c * 9 / 5) + 32


@log_execution
def fahrenheit_to_celsius(f: float) -> float:
    """Convert Fahrenheit to Celsius.

    Args:
        f (float): Temperature in Fahrenheit

    Returns:
        float: Temperature in Celsius
    """
    return (f - 32) * 5 / 9
