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

for th in range(a1, b1 + 1):
    if th % 2 != 0:
        for hun in range(a2, b2 + 1):
            if hun % 2 != 0:
                for de in range(a3, b3 + 1):
                    if de % 2 != 0:
                        for ed in range(a4, b4+1):
                            if ed % 2 != 0:
                                print(f'{th}{hun}{de}{ed}', end=' ')
