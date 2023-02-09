first_number = input()
last_number = input()
a1 = int(first_number[0])
a2 = int(first_number[1])
a3 = int(first_number[2])
a4 = int(first_number[3])
b1 = int(last_number[0])
b2 = int(last_number[1])
b3 = int(last_number[2])
b4 = int(last_number[3])
for thousands in range(a1, b1 + 1):
    if thousands % 2 == 0:
        continue
    for hundreds in range(a2, b2 + 1):
        if hundreds % 2 == 0:
            continue
        for decimals in range(a3, b3 + 1):
            if decimals % 2 == 0:
                continue
            for last in range(a4, b4 + 1):
                if last % 2 == 0:
                    continue
                print(str(thousands) + str(hundreds) + str(decimals) + str(last), end=' ')
