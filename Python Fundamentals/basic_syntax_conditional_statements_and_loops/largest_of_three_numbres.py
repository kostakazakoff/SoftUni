numbers = []
for i in range(3):
    number = int(input())
    numbers.append(number)
largest_number = sorted(numbers)[-1]
print(largest_number)
