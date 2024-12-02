operation = input()
a = int(input())
b = int(input())


def calculation(x, y, operator):
    if operator == 'multiply':
        return x * y
    elif operator == 'divide':
        return x // y
    elif operator == 'add':
        return x + y
    elif operator == 'subtract':
        return x - y


print(calculation(a, b, operation))
