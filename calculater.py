class Calculater:

    def __init__(self, num1, num2):
        try:
            self.num1 = int(num1)
            self.num2 = int(num2)
        except TypeError:
            raise TypeError

    def plus(self):
        return self.num1 + self.num2

    def minus(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2


result = Calculater(2, 1)

print(result.minus())
