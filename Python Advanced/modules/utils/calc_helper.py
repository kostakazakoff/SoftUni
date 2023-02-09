from math import log, e


def calc_logarithm(n: int, b: str):
    b = int(b) if b.isdigit() else e
    return log(n, b)


def add(x: float, y: int):
    return x + y


def sub(x: float, y: int):
    return x - y


def mult(x: float, y: int):
    return x * y


def div(x: float, y: int):
    try: return x / y
    except ZeroDivisionError: print('Can not divide by zero')


def pow(x: float, y: int):
    return x ** y
    


def calc_expression(expression: str):
    try: n_float, operator, n_int = float(expression.split()[0]), expression.split()[1], int(expression.split()[2])
    except ValueError:
        print('The second number must be an integer')
        return
    operations = {
        '/': div(n_float, n_int),
        '*': mult(n_float, n_int),
        '-': sub(n_float, n_int),
        '+': add(n_float, n_int),
        '^': pow(n_float, n_int)
    }
    try: return operations[operator]
    except KeyError: print('Not a valid operator')