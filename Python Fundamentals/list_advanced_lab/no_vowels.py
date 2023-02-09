str = input()


def no_vowels(input_string: str):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return ''.join([ch for ch in input_string if ch.lower() not in vowels])


print(no_vowels(str))