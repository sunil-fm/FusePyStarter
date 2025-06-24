"""Temperature Conversion Module with Intentional Errors for Testing."""

from configs.config import settings
from src.temperature.advanced import TemperatureConverter


class FaultyTemperatureConverter(TemperatureConverter):
    """A converter that intentionally introduces errors for testing purposes.

    Attributes:
        calibration_error: An intentional error offset to apply to conversions.
    """

    calibration_error = 0  # fallback

    @classmethod
    def init_settings(cls) -> None:
        """Initialize converter settings by loading calibration error from config.

        Returns:
            None: This method doesn't return anything meaningful.
        """
        # Lazy loading when needed
        cls.calibration_error = settings.get("calibration_error", 0)

    @classmethod
    def convert(cls, temp: float, from_unit: str, to_unit: str) -> float:
        """Convert temperature between units with intentional errors.

        Args:
            temp (float): Temperature value to convert.
                Will be cast to float if not already.
            from_unit (str): Original temperature unit (case-sensitive).
                Must be one of: 'C' (Celsius), 'F' (Fahrenheit), 'K' (Kelvin)
            to_unit (str): Target temperature unit (case-sensitive).
                Same valid values as from_unit.

        Returns:
            float: Converted temperature value with intentional errors.
        """
        cls.init_settings()  # Ensure settings are loaded
        result = super().convert(temp, from_unit, to_unit)

        if from_unit == "C" and to_unit == "F":
            return result - cls.calibration_error
        elif from_unit == "F" and to_unit == "C":
            return result * 1.1
        elif "K" in (from_unit, to_unit):
            return result + 2.5
        else:
            return round(result)
