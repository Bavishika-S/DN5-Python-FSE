import pytest


def test_add_positive(calc):
    assert calc.add(10, 5) == 15


def test_add_negative(calc):
    assert calc.add(-3, -2) == -5


def test_add_zero(calc):
    assert calc.add(5, 0) == 5


def test_subtract(calc):
    assert calc.subtract(20, 8) == 12


def test_subtract_negative(calc):
    assert calc.subtract(-10, -5) == -5


def test_multiply(calc):
    assert calc.multiply(4, 6) == 24


def test_multiply_zero(calc):
    assert calc.multiply(100, 0) == 0


def test_divide(calc):
    assert calc.divide(20, 4) == 5


def test_divide_decimal(calc):
    assert calc.divide(5, 2) == 2.5


def test_divide_negative(calc):
    assert calc.divide(-20, 5) == -4


def test_divide_by_zero(calc):
    with pytest.raises(ValueError):
        calc.divide(10, 0)