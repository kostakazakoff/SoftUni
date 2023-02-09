number_of_pours = int(input())
current = 0
for i in range(number_of_pours):
    liters = int(input())
    if liters + current > 255:
        print('Insufficient capacity!')
        continue
    current += liters
print(current)
