from src import __version__
from src.calculator import add


def test_version():
    assert __version__ == "0.1.0"


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-2, -3) == -5


def test_add_mixed_sign_numbers():
    assert add(-2, 3) == 1


def test_add_zero():
    assert add(0, 5) == 5
    assert add(5, 0) == 5
