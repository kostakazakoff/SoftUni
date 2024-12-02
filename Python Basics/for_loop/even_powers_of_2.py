n = int(input())

for power in range (n+1):
    if power % 2 == 0:
        result = 2 ** power
        print(result)