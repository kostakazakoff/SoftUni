def valid(index_to_check: int):
    if 0 <= index_to_check < len(travel_stops):
        return True
    return False


def add_stop(string, add_index: int, destination: str):
    if valid(add_index):
        string = f'{string[:add_index]}{destination}{string[add_index:]}'
    return string


def remove_stop(string, start: int, end: int):
    if valid(start) and valid(end):
        string = f'{string[:start]}{string[end + 1:]}'
    return string


def switch(string, old: str, new: str):
    if old in string:
        string = string.replace(old, new)
    return string


travel_stops = input()

command = input()
while command != 'Travel':
    manipulation, *variables = command.split(':')
    if manipulation == 'Add Stop':
        index, string_to_add = variables
        travel_stops = add_stop(travel_stops, int(index), string_to_add)
        print(travel_stops)
    elif manipulation == 'Remove Stop':
        start_index, end_index = variables
        travel_stops = remove_stop(travel_stops, int(start_index), int(end_index))
        print(travel_stops)
    else:
        old_string, new_string = variables
        travel_stops = switch(travel_stops, old_string, new_string)
        print(travel_stops)
    command = input()

print(f'Ready for world tour! Planned stops: {travel_stops}')
