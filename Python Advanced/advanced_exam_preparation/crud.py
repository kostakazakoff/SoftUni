def move_to(direction):
    global pos_r, pos_c
    if direction == 'up': pos_r -= 1
    elif direction == 'down': pos_r += 1
    elif direction == 'left': pos_c -= 1
    elif direction == 'right': pos_c += 1


def c():
    global matrix, pos_r, pos_c, parameters
    if matrix[pos_r][pos_c] == '.':
        matrix[pos_r][pos_c] = parameters[-1]


def r():
    global matrix, pos_r, pos_c
    if matrix[pos_r][pos_c] != '.':
        print(matrix[pos_r][pos_c])


def u():
    global matrix, pos_r, pos_c
    if matrix[pos_r][pos_c] != '.':
        matrix[pos_r][pos_c] = parameters[-1]


def d():
    global matrix, pos_r, pos_c
    matrix[pos_r][pos_c] = '.'


def operation():
    global current_operation
    if current_operation == 'Create': c()
    elif current_operation == 'Read': r()
    elif current_operation == 'Update': u()
    elif current_operation == 'Delete': d()      


SIZE = 6
matrix = [input().split() for _ in range(SIZE)]
pos_r, pos_c = eval(input())

current_operation, *parameters = input().split(', ')
while current_operation != 'Stop':
    move_to(parameters[0])
    operation()
    current_operation, *parameters = input().split(', ')

[print(*row) for row in matrix]