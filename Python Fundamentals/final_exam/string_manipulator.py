def translate(the_string: str, the_char: str, the_replacement: str):
    the_string = the_string.replace(the_char, the_replacement)
    print(the_string)
    return the_string


def includes(the_string: str, the_substring: str):
    if the_substring in the_string:
        return True
    return False


def check_start(the_string: str, the_substring: str):
    length = len(the_substring)
    if the_string[:length] == the_substring:
        return True
    return False


def lowercase(the_string: str):
    the_string = the_string.lower()
    print(the_string)
    return the_string


def find_index(the_string: str, the_char: str):
    for i in range(len(the_string) - 1, -1, -1):
        if the_char == the_string[i]:
            return i


def remove(the_string: str, start_index: int, the_count: int):
    the_string = f'{the_string[:start_index]}{the_string[start_index+the_count:]}'
    print(the_string)
    return the_string


string = input()

command = input()
while command != 'End':
    action, *info = command.split()
    if action == 'Translate':
        char = info[0]
        replacement = info[1]
        string = translate(string, char, replacement)
    elif action == 'Includes':
        substring = info[0]
        print(includes(string, substring))
    elif action == 'Start':
        substring = info[0]
        print(check_start(string, substring))
    elif action == 'Lowercase':
        string = lowercase(string)
    elif action == 'FindIndex':
        char = info[0]
        print(find_index(string, char))
    elif action == 'Remove':
        start, count = [int(x) for x in info]
        string = remove(string, start, count)
    command = input()
