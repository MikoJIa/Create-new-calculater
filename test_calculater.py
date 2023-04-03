import pytest

from calculater import calc_plus, calc_minus, calc_division, calc_multiply, \
    calc_exponent

@pytest.mark.parametrize(
    'num1, num2, result',
    [
        (2, 2, 4),
        (2, -2, 0),
        (2, 0, 2)
    ]
)
def test_calc_plus(num1, num2, result):
    assert calc_plus(num1, num2) == result
