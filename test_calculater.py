import pytest

from calculater import calc_plus, calc_minus, calc_division, calc_multiply, \
    calc_exponent

@pytest.mark.parametrize(
    'num1, num2, sign, result',
    [
        (2, 2, '+', 4),
        (2, -2, '+', 0),
        (2, 0, '+', 2)
    ]
)
def test_calc_plus(num1, num2, sign, result):
    assert calc_plus(num1, num2) == result


@pytest.mark.parametrize(
    'num1, num2, sign, result',
    [
        (2, 1, '-', 1),
        (3, 2, '-', 1),
        (2, 0, '-', 2)
    ]
)
def test_calc_minus(num1, num2, sign, result):
    assert calc_minus(num1, num2) == result


