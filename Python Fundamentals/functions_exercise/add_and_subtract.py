def add_and_subtract(x, y, z):

    def add():
        add_result = x + y
        return add_result

    def subtract():
        subtract_result = add() - z
        return subtract_result

    return subtract()


a = int(input())
b = int(input())
c = int(input())

print(add_and_subtract(a, b, c))
