import math

figure = input()
a = float(input())

if figure == "square":
    area = a ** 2
elif figure == "rectangle":
    b = float(input())
    area = a * b
elif figure == "circle":
    area = math.pi * a ** 2
elif figure == "triangle":
    h = float(input())
    area = a * h / 2

print(f'{area:.3f}')