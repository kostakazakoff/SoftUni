def rectangle(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        return 'Enter valid values!'
    return f'Rectangle area: {a * b}\nRectangle perimeter: {2 * a + 2 * b}'


print(rectangle(2, 10))