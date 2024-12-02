def first_or_second():
    global parameters, first_sequence, second_sequence
    if parameters[0] == 'First':
        return first_sequence
    return second_sequence


def add_numbers():
    global parameters, first_sequence, second_sequence
    sequence = first_or_second()
    sequence.update({x for x in parameters[1::]})


def remove_numbers():
    global parameters, first_sequence, second_sequence
    sequence = first_or_second()
    [sequence.discard(x) for x in parameters[1::]]


def check_subset():
    global first_sequence, second_sequence
    return first_sequence <= second_sequence or second_sequence <= first_sequence


first_sequence, second_sequence = [set(map(int, input().split())) for _ in range(2)]
number_of_commands = int(input())
for _ in range(number_of_commands):
    action, *parameters = [int(x) if x.isdigit() else x for x in input().split()]
    if action == 'Add':
        add_numbers()
    elif action == 'Remove':
        remove_numbers()
    else:
        print(check_subset())

print(', '.join(map(str, sorted(first_sequence))))
print(', '.join(map(str, sorted(second_sequence))))
