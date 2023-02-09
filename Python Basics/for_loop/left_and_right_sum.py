n = int(input())
first_sum = 0
second_sum = 0
for i in range(n):
    number = int(input())
    first_sum += number
for i in range (n):
    number = int(input())
    second_sum += number
diff = abs(first_sum - second_sum)
if first_sum == second_sum:
    print(f'Yes, sum = {first_sum}')
else:
    print(f'No, diff = {diff}')