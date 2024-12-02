def convert_to_dict(string: str):
    result = []
    value = ''
    key = ''
    for i in range(len(string) - 1):
        if not string[i].isdigit():
            value += string[i].upper()
        else:
            key += string[i]
            if not string[i + 1].isdigit():
                key = int(key)
                result.append({key: value})
                value = ''
                key = ''
    key += string[-1]
    result.append({int(key): value})
    return result


player_string = input()
unique_count = 0
nums_count = 0
result_list = []
tokens = convert_to_dict(player_string)

for token in tokens:
    result_list += [k * v for k, v in token.items()]
output = ''.join(result_list)

print(f'Unique symbols used: {len(set(output))}')
print(output)
