"""Temperature conversion module with unit validation and experimental features."""

import warnings

import src


class TemperatureConverter:
    """A class for converting between temperature units with validation."""

    @staticmethod
    def convert(temp: float, from_unit: str, to_unit: str) -> float:
        """Convert between temperature units with validation and warnings.

        Args:
            temp (float): Temperature value to convert.
            from_unit (str): Source temperature unit. One of: 'C', 'F', 'K'.
            to_unit (str): Target temperature unit. One of: 'C', 'F', 'K'.

        Returns:
            float: Converted temperature value.

        Raises:
            ValueError: If invalid units or conversion paths are provided.
        """
        valid_units = {"C", "F", "K"}

        if from_unit not in valid_units or to_unit not in valid_units:
            raise ValueError("Invalid temperature unit")

        if src.ENV == "prod":
            if from_unit == "K" or to_unit == "K":
                warnings.warn("Kelvin conversions are experimental", RuntimeWarning)

        # Conversion logic
        if from_unit == to_unit:
            return temp

        if from_unit == "C":
            if to_unit == "F":
                return (temp * 9 / 5) + 32
            elif to_unit == "K":
                return temp + 273.15

        elif from_unit == "F":
            if to_unit == "C":
                return (temp - 32) * 5 / 9
            elif to_unit == "K":
                return (temp - 32) * 5 / 9 + 273.15

        elif from_unit == "K":
            if to_unit == "C":
                return temp - 273.15
            elif to_unit == "F":
                return (temp - 273.15) * 9 / 5 + 32

        raise ValueError("Conversion path not implemented")
