n = int(input())
even_sum = 0
odd_sum = 0
for i in range (n):
    number = int(input())
    if i % 2 == 0:
        even_sum += number
    else:
        odd_sum += number
diff = abs(even_sum - odd_sum)
if even_sum == odd_sum:
    print('Yes')
    print(f'Sum = {even_sum}')
else:
    print('No')
    print(f'Diff = {diff}')