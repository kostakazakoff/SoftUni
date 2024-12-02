def sorted_int(string):
    numbers = [int(x) for x in string.split()]
    return sorted(numbers)


string_of_numbers = input()
print(sorted_int(string_of_numbers))
