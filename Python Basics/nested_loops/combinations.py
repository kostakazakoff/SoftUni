num = int(input())
count = 0
for x1 in range(num + 1):
    for x2 in range(num + 1):
        for x3 in range(num + 1):
            if x1 + x2 + x3 != num:
                continue
            else:
                count += 1
print(count)