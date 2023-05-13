from exception import NumberError, MyException, MyZeroDivisionError

class Calculater:

    def __init__(self, num1, num2):
        if isinstance(num1, int) and isinstance(num2, int):
            self.num1 = int(num1)
            self.num2 = int(num2)
        else:
            raise MyException('Вводимые данные должны соответствовать типу int ')

    def plus(self):
        return self.num1 + self.num2

    def minus(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def division(self) -> float:
        try:
            self.num1 / self.num2
        except ZeroDivisionError:
            raise MyZeroDivisionError


a = Calculater(1, 1)
# print(a.plus())
# #
# print(result.division())

