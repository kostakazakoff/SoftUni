number_of_strings = int(input())
exclusives = [',', '.', '_']

for _ in range(number_of_strings):
    string = input()
    if any(x in exclusives for x in string):
        print(f'{string} is not pure!')
    else:
        print(f'{string} is pure.')
