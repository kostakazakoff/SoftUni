import sys

n = int(input())
sum_numbers = 0
max_num = -sys.maxsize
for i in range(n):
    number = int(input())
    if number > max_num:
        max_num = number # the biggest number in the range
    sum_numbers += number # total sum, including max_num
comp_sum_numbers = sum_numbers - max_num # compared sum
diff = abs(comp_sum_numbers - max_num)
if max_num == comp_sum_numbers:
    print('Yes')
    print(f'Sum = {sum_numbers - max_num}')
else:
    print('No')
    print(f'Diff = {diff}')
