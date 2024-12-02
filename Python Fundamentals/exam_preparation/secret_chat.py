def insert_space(string: str, index_to_insert: int):
    string = f'{string[:index_to_insert]} {string[index_to_insert:]}'
    print(string)
    return string


def reverse_string(string: str, substring_to_move: str):
    if substring_to_move in string:
        string = string.replace(substring_to_move, '', 1)
        string = f'{string}{substring_to_move[::-1]}'
        print(string)
        return string
    print('error')
    return string


def change_all(string: str, substring_to_replace: str, replacement_text: str):
    if substring_to_replace in string:
        string = string.replace(substring_to_replace, replacement_text)
        print(string)
    return string


message = input()

command = input()
while command != 'Reveal':
    manipulation, *str_index = command.split(':|:')
    if manipulation == 'InsertSpace':
        index = int(str_index[0])
        message = insert_space(message, index)
    elif manipulation == 'Reverse':
        substring = str_index[0]
        message = reverse_string(message, substring)
    else:
        substring, replacement = str_index
        message = change_all(message, substring, replacement)
    command = input()

print(f'You have a new text message: {message}')