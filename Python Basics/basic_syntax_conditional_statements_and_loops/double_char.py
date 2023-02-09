string = input()
while string != 'End':
    if string != 'SoftUni':
        for s in string:
            print(2 * s, end='')
        print()
    string = input()