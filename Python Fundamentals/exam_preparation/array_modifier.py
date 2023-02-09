def swap_elements(array: list, index_1: int, index_2: int):
    array[index_1], array[index_2] = array[index_2], array[index_1]
    return array


def multiply_elements(array: list, index_1: int, index_2: int):
    array[index_1] *= array[index_2]
    return array


def decrease_elements(array: list):
    array = [(number - 1) for number in array]
    return array


numbers = list(map(int, input().split(' ')))
command = input()

while command != 'end':
    command = command.split(' ')
    operation = command[0]
    if operation == 'swap':
        i_1 = int(command[1])
        i_2 = int(command[2])
        numbers = swap_elements(numbers, i_1, i_2)
    elif operation == 'multiply':
        i_1 = int(command[1])
        i_2 = int(command[2])
        numbers = multiply_elements(numbers, i_1, i_2)
    elif operation == 'decrease':
        numbers = decrease_elements(numbers)
    command = input()

print(', '.join(list(map(str, numbers))))