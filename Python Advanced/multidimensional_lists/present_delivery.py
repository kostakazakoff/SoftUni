def in_matrix(r, c):
    global size
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


def move(direction: str, r, c):
    if direction == 'up':
        r -= 1
    elif direction == 'down':
        r += 1
    elif direction == 'left':
        c -= 1
    elif direction == 'right':
        c += 1
    return r, c


def gift(r, c):
    global nice_kids_left, happy_kids, presents, matrix
    if matrix[r][c] == 'V':
        nice_kids_left -= 1
        happy_kids += 1
        presents -= 1
    elif matrix[r][c] == 'X' and happy_santa:
        presents -= 1
    matrix[r][c] = '-'
    
    
presents = int(input())
size = int(input())
matrix = []
nice_kids_left = 0
happy_kids = 0

#-------------------------------------------------------------------
for row in range(size):
    col = input().split()
    for idx, element in enumerate(col):
        if element == 'S':
            santa_r, santa_c = row, idx
            col[idx] = '-'
        elif element == 'V':
            nice_kids_left += 1
    matrix.append(col)


#--------------------------------------------------------------------
direction = input()
while direction != 'Christmas morning':
    new_pos_r, new_pos_c = move(direction, santa_r, santa_c)
    happy_santa = False

    if not in_matrix(new_pos_r, new_pos_c):
        continue

    santa_r, santa_c = new_pos_r, new_pos_c

    if matrix[santa_r][santa_c] == 'C':
        happy_santa = True

        for direct in ('up', 'down', 'left', 'right'):
            pos_r, pos_c = move(direct, santa_r, santa_c)
            gift(pos_r, pos_c)

            if not presents:
                break

    else:
        gift(santa_r, santa_c)

    if not presents:
        break
    

    direction = input()

#------------------------------------------------------------------
matrix[santa_r][santa_c] = 'S'

if not presents and nice_kids_left:
    print('Santa ran out of presents!')
[print(*row) for row in matrix]
if not nice_kids_left:
    print(f'Good job, Santa! {happy_kids} happy nice kid/s.')
else:
    print(f'No presents for {nice_kids_left} nice kid/s.')
