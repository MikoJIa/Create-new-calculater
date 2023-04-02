def calc_plus(num1: int, num2: int) -> int | float:
    return num1 + num2


def calc_minus(num1: int, num2: int) -> int | float:
    return num1 - num2


def calc_division(num1: int, num2: int) -> int | float:
    return num1 / num2


def calc_multiply(num1: int, num2: int) -> int | float:
    return num1 * num2


def calc_exponent(num1: int, num2: int) -> int | float:
    return num1 ** num2


print('Welcome to calculater!!!')
print('Choose one of the calculation options' + '\n'
                                                '+: plus\n'
                                                '-: minus\n'
                                                '/: division\n'
                                                '*: multiply\n'
                                                '**: exponent\n')


symbol = ['+', '-', '/', '*', '**']
try:
    num1 = int(input('Enter the first number - '))
    sign = input('Enter symbol operator - ')
    while sign not in symbol:
        print(f'Enter one of the operators {symbol}')
        sign = input('Enter symbol operator - ')
    if sign in symbol:
        num2 = int(input('Enter the second number - '))
        if sign == '+':
            print(f'{num1} + {num2} = {calc_plus(num1, num2)}')
        elif sign == '-':
            print(f'{num1} - {num2} = {calc_minus(num1, num2)}')
        elif sign == '/':
            print(f'{num1} / {num2} = {calc_division(num1, num2)}')
        elif sign == '*':
            print(f'{num1} * {num2} = {calc_multiply(num1, num2)}')
        elif sign == '**':
            print(f'{num1} ** {num2} = {calc_exponent(num1, num2)}')
except (TypeError, ValueError):
    print('The value contain 2 integers and 1 allowed character')



