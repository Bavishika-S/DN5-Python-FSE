import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


def test_add(calc):
    assert calc.add(10, 5) == 15


def test_subtract(calc):
    assert calc.subtract(10, 5) == 5


def test_multiply(calc):
    assert calc.multiply(10, 5) == 50


def test_divide(calc):
    assert calc.divide(10, 5) == 2


def test_divide_by_zero(calc):
    with pytest.raises(ValueError):
        calc.divide(10, 0)