def factorial(integer):
    if integer == 0:
        integer = 1
    for n in range(1, integer):
        integer *= n
    return integer


int_1 = int(input())
int_2 = int(input())
division = factorial(int_1) / factorial(int_2)
print(f'{division:.2f}')
