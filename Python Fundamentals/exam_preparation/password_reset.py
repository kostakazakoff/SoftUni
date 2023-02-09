def take_odd(string: str):
    string = ''.join([string[i] for i in range(len(string)) if i % 2 != 0])
    print(string)
    return string


def cut_from_string(string: str):
    string = f'{string[:index]}{string[index + length:]}'
    print(string)
    return string


def replace_substitute(string: str):
    if substring not in string:
        print('Nothing to replace!')
        return string
    string = string.replace(substring, substitute)
    print(string)
    return string


password = input()

command = input()

while command != 'Done':
    action, *info = command.split()
    if action == 'TakeOdd':
        password = take_odd(password)
    elif action == 'Cut':
        index, length = [int(x) for x in info]
        password = cut_from_string(password)
    elif action == 'Substitute':
        substring, substitute = info
        password = replace_substitute(password)

    command = input()

print(f'Your password is: {password}')
