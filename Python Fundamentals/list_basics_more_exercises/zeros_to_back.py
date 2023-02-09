numbers = input()
numbers = list(int(n) for n in numbers.split(', '))
zeros = [x for x in numbers if x == 0]
numbers_no_zeros = [x for x in numbers if x != 0]
reordered = numbers_no_zeros + zeros
print(reordered)
