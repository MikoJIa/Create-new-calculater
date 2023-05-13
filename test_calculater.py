import pytest
from calculater import Calculater
from exception import MyZeroDivisionError

@pytest.mark.parametrize("num1, num2, result", [(2, 2, 4), (2, -2, 0), (2, 0, 2)])
def test_plus(num1, num2, result):
    a1 = Calculater(num1, num2)
    assert a1.plus() == result


@pytest.mark.parametrize("num1, num2, result", [(2, 2, 0), (2, -2, 4), (2, 0, 2)])
def test_minus(num1, num2, result):
    a2 = Calculater(num1, num2)
    assert a2.minus() == result


@pytest.mark.parametrize("num1, num2, result", [(2, 2, 4), (2, -2, -4), (2, 0, 0)])
def test_multiply(num1, num2, result):
    a3 = Calculater(num1, num2)
    assert a3.multiply() == result


@pytest.mark.parametrize("num1, num2, result", [(2, 0, MyZeroDivisionError)])
def test_zero_division_error(num1, num2, result):
    a4 = Calculater(num1, num2)
    with pytest.raises(MyZeroDivisionError):
        assert 2 == 2
        a4.division()


@pytest.mark.parametrize('num1, num2, result', [(2, 2, 1), (4, -2, -2), (150, 50, 3)])
def test_division(num1, num2, result):
    a5 = Calculater(num1, num2)
    assert a5.division() == result
