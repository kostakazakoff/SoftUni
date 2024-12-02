def print_digits(string: str):
    print(''.join([x for x in string if x.isdigit()]))


def print_alphabetic(string: str):
    print(''.join([x for x in string if x.isalpha()]))


def print_others(string: str):
    print(''.join([x for x in string if not x.isalpha() and not x.isdigit()]))


text = input()
print_digits(text)
print_alphabetic(text)
print_others(text)

