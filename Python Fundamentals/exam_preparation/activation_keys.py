def if_contains(the_substring: str):
    if the_substring not in activation_key:
        print('Substring not found!')
        return
    print(f'{activation_key} contains {the_substring}')


def flip_simbols(the_string: str, up_low: str, start_index: int, end_index: int):
    if up_low == 'Upper':
        the_string = f'{the_string[:start_index]}{the_string[start_index:end_index].upper()}{the_string[end_index:]}'
    else:
        the_string = f'{the_string[:start_index]}{the_string[start_index:end_index].lower()}{the_string[end_index:]}'
    print(the_string)
    return the_string


def slice_string(the_string: str, start_index: int, end_index: int):
    the_string = f'{the_string[:start_index]}{the_string[end_index:]}'
    print(the_string)
    return the_string


activation_key = input()
command = input()
while command != 'Generate':
    action, *info = command.split('>>>')

    if action == 'Contains':
        substring = info[0]
        if_contains(substring)

    elif action == 'Flip':
        up_or_low, start, end = [int(s) if s.isdigit() else s for s in info]
        activation_key = flip_simbols(activation_key, up_or_low, start, end)

    elif action == 'Slice':
        start, end = [int(s) for s in info]
        activation_key = slice_string(activation_key, start, end)

    command = input()

print(f'Your activation key is: {activation_key}')
