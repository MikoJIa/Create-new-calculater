class MyZeroDivisionError(ZeroDivisionError):
    '''Выбрасывается когда делительт равен нулю'''
    pass

class NumberError(Exception):
    '''Число не соответсвует типу int'''
    pass


class MyException(Exception):
    pass

def divide(a: int, b: int) -> int | float:

    if not isinstance(a, int) or not isinstance(b, int):
        raise NumberError('Число должно быть целым')
    if b == 0:
        raise MyZeroDivisionError('Делитель должен быть больше нуля')
    return a / b


if __name__ == '__main__':
    print(divide(2, 1.1))