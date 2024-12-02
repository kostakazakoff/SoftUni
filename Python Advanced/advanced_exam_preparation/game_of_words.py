def step_to(d: str, r, c):
    if d == 'up': r -= 1
    elif d == 'down': r += 1
    elif d == 'left': c -= 1
    elif d == 'right': c += 1
    return r, c


init_string = input()
SIZE = int(input())
matrix = []

for row in range(SIZE):
    line = list(input())
    if 'P' in line:
        pos_r, pos_c = row, line.index('P')
        line[pos_c] = '-'
    matrix.append(line)
    
number_of_commands = int(input())

for i in range(number_of_commands):
    direction = input()
    target_r, target_c = step_to(direction, pos_r, pos_c)

    if not 0 <= target_r < SIZE or not 0 <= target_c < SIZE:
       if init_string: init_string = init_string[:-1]
       continue

    matrix[pos_r][pos_c] = '-'
    pos_r, pos_c = target_r, target_c

    if matrix[pos_r][pos_c] != '-': init_string += matrix[pos_r][pos_c]

matrix[pos_r][pos_c] = 'P'
print(init_string)
[print(''.join(x)) for x in matrix]
