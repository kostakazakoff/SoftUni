def swap():
    global command, matrix
    command = command.split()

    if valid_command(*command):
        source_r, source_c, dest_r, dest_c = [int(x) for x in command[1:]]
        
        if valid_coordinates(source_r, source_c) and valid_coordinates(dest_r, dest_c):
            matrix[source_r][source_c], matrix[dest_r][dest_c] = matrix[dest_r][dest_c], matrix[source_r][source_c]
            [print(*r) for r in matrix]


def valid_command(*args):
    if len(args) != 5 or args[0] != 'swap' or not all([n.isdigit() for n in args[1:]]):
        print("Invalid input!")
        return False
    return True


def valid_coordinates(r, c):
    global rows, cols
    if 0 <= r < rows and 0 <= c < cols:
        return True
    print("Invalid input!")
    return False


rows, cols = [int(x) for x in input().split()]
matrix = [[c for c in input().split()] for rows in range(rows)]

command = input()
while command != 'END':
    swap()

    command = input()