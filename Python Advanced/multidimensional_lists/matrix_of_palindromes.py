def letters(r, c):
    first_last_letter = chr(r + 97)
    mid_letter = chr(r + c + 97)
    return f'{first_last_letter}{mid_letter}{first_last_letter}'


rows, cols = [int(x) for x in input().split()]
matrix = [[letters(row, col) for col in range(cols)] for row in range(rows)]

[print(*r) for r in matrix]
