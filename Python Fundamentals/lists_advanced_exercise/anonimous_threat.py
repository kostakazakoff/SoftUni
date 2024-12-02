def merge(source: list, start_index: int, end_index: int):
    if start_index < 0:
        start_index = 0
    source[start_index:end_index + 1] = [''.join(source[start_index:end_index + 1])]
    return source


def divide(source: list, index: int, partitions: int):
    divided_str = ''
    str_to_divide = source[index]
    if partitions <= 1 or partitions > len(str_to_divide):
        return source
    step = len(str_to_divide) // partitions
    source_start = source[:index]
    source_end = source[index + 1:]
    while len(str_to_divide) > 0:
        divided_str += str_to_divide[:step] + ' '
        str_to_divide = str_to_divide[step:]
    divided_str = (divided_str.strip())
    divided_list = divided_str.split()
    if len(divided_list) > partitions:
        divided_list = divided_list[:-2] + [''.join(divided_list[-2:])]
    return source_start + divided_list + source_end


threat_list = input().split()
command = input()

while command != '3:1':
    command = command.split()
    action = command[0]
    start = int(command[1])
    if action == 'merge':
        end = int(command[2])
        threat_list = merge(threat_list, start, end)
    elif action == 'divide':
        parts = int(command[2])
        threat_list = divide(threat_list, start, parts)

    command = input()

print(*threat_list)
