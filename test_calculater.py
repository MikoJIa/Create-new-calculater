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


@pytest.mark.parametrize(
    'num1, num2, sign, result',
    [
        (10, 2, '/', 5),
        (10, 5, '/', 2),
        (5, 2, '/', 2.5)
    ]
)
def test_calc_division(num1, num2, sign, result):
    assert calc_division(num1, num2) == result

@pytest.mark.parametrize(
    'num1, num2, sign, result',
    [
        (10, 0, '/', ZeroDivisionError)
    ]
)
def test_Zero_Division_Error(num1, num2, sign, result):
    with pytest.raises(result):
        assert calc_division(num1, num2) == result

@pytest.mark.parametrize(
    'num1, num2, sign, result',
    [
        (10, 2, '*', 20),
        (10, -2, '*', -20),
        (-10, -2, '*', 20)
    ]
)
def test_calc_multiply(num1, num2, sign, result):
    assert calc_multiply(num1, num2) == result

@pytest.mark.parametrize(
    'num1, num2, sign, result',
    [
        (2, 2, '**', 4),
        (2, -2, '**', 0.25),
        (-2, 2, '**', 4)
    ]
)
def test_calc_exponent(num1, num2, sign, result):
    assert calc_exponent(num1, num2) == result
