n = int(input())
count = 1
counted = False
for row in range(1, n + 1):
    if counted:
        break
    for col in range(1, row + 1):
        print(count, end=' ')
        count += 1
        if count > n:
            counted = True
            break
    print()