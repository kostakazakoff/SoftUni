secret = input()
secret = str(secret)
bulls = int(input())
cows = int(input())
solution = False
for n1 in range(1, 10):
    for n2 in range(1, 10):
        for n3 in range(1, 10):
            for n4 in range(1, 10):
                my_number = str(n1) + str(n2) + str(n3) + str(n4)
                my_number_copy = list(my_number)
                secret_copy = list(secret)
                bulls_counter = 0
                cows_counter = 0
                for each in range (4):
                    if my_number_copy[each] == secret_copy[each]:
                        my_number_copy[each] = 'x'
                        secret_copy[each] = 'y'
                        bulls_counter += 1
                if bulls_counter < 3:
                    for i in range (4):
                        for j in range(4):
                            if my_number_copy[i] == secret_copy[j]:
                                my_number_copy[i] = 'a'
                                secret_copy[j] = 'b'
                                cows_counter += 1
                if bulls_counter == bulls and cows_counter == cows:
                    solution = True
                    print(my_number, end=' ')
if not solution:
    print('No')