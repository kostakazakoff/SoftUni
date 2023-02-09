numbers_dict = {}

key = input()
while key != 'Search':
    try:
        value = int(input())
        numbers_dict[key] = value
    except ValueError:
        print("The variable number must be an integer")
    key = input()

key = input()
while key != 'Remove':
    try:
        print(numbers_dict[key])
    except KeyError:
        print("Number does not exist in dictionary")
    key = input()

key = input()
while key != 'End':
    try:
        del numbers_dict[key]
    except KeyError:
        print("Number does not exist in dictionary")
    key = input()

print(numbers_dict)
