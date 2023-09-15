def calc_factorial(n):
    if n <= 1:
        return 1
    return n * calc_factorial(n - 1)

number = int(input())
print(calc_factorial(number))