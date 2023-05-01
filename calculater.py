from exception import NumberError, MyException

class Calculater:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        try:
            if not isinstance(self.num1, int) or not isinstance(self.num2, int):
                raise MyException('Вводимые данные должны соответствовать типу int ')
        except ValueError:
            raise MyException('Вводимые данные должны соответствовать типу int ')

    def plus(self):
        return self.num1 + self.num2

    def minus(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def division(self) -> int | float:
        return self.num1 / self.num2


# a = Calculater(2, '1')
# print(a.plus())
# #
# print(result.division())

