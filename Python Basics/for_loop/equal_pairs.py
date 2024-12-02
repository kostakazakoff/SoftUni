import sys

number_of_pairs = int(input())
first_pair_sum = 0
second_pair_sum = 0
diff = 0
equal = True
max = -sys.maxsize
for count in range(number_of_pairs):
    first = int(input())
    second = int(input())
    if count % 2 == 0:
        first_pair_sum = first + second
    else:
        second_pair_sum = first + second
    if count >= 1:
        if first_pair_sum != second_pair_sum:
            equal = False
            diff = abs(first_pair_sum - second_pair_sum)
            if diff > max:
                max = diff

if equal:
    print(f'Yes, value={first_pair_sum}')
else:
    print(f'No, maxdiff={max}')