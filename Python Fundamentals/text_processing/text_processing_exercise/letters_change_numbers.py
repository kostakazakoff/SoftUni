def string_content(strng: str):
    first_letter = strng[0]
    last_letter = strng[-1]
    number = strng[1:-1]
    return first_letter, last_letter, int(number)


def operation(strng: str):
    result = 0
    first, last, num = string_content(strng)
    if first.isupper():
        first_position = ord(first) - 64
        result = num / first_position
    elif first.islower():
        first_position = ord(first) - 96
        result = num * first_position
    if last.isupper():
        last_position = ord(last) - 64
        result -= last_position
    elif last.islower():
        last_position = ord(last) - 96
        result += last_position
    return result


strings = input().split()
total = 0

for string in strings:
    string = string.strip()
    current_result = operation(string)
    total += current_result

print(f'{total:.2f}')
