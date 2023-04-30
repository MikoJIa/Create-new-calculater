import pytest
from calculater import Calculater


@pytest.mark.parametrize("num1, num2, result", [(2, 2, 4), (2, -2, 0), (2, 0, 2)])
def test_plus(num1, num2, result):
    a1 = Calculater(num1, num2)
    assert a1.plus() == result


@pytest.mark.parametrize("num1, num2, result", [(2, 2, 0), (2, -2, 4), (2, 0, 2)])
def test_minus(num1, num2, result):
    a1 = Calculater(num1, num2)
    assert a1.minus() == result
