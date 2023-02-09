import sys

n = int(input())
even_max = -sys.maxsize
odd_max = -sys.maxsize
even_min = sys.maxsize
odd_min = sys.maxsize
even_sum = 0
odd_sum = 0
there_is_odd = False
there_is_even = False
for i in range(1, n + 1):
    number = float(input())
    if i % 2 != 0:
        odd_sum += number
        there_is_odd = True
        if number > odd_max:
            odd_max = number
        if number < odd_min:
            odd_min = number
    else:
        even_sum += number
        there_is_even = True
        if number > even_max:
            even_max = number
        if number < even_min:
            even_min = number

print(f'OddSum={odd_sum:.2f},')
if there_is_odd:
    print(f'OddMin={odd_min:.2f},')
    print(f'OddMax={odd_max:.2f},')
else:
    print(f'OddMin=No,')
    print(f'OddMax=No,')
print(f'EvenSum={even_sum:.2f},')
if there_is_even:
    print(f'EvenMin={even_min:.2f},')
    print(f'EvenMax={even_max:.2f}')
else:
    print(f'EvenMin=No,')
    print(f'EvenMax=No')