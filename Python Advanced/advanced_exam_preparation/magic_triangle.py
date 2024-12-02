def get_magic_triangle(rows):
    sequence = []
    for row in range(rows):
        current_row = [None] * (row + 1)
        current_row[0], current_row[-1] = 1, 1
        for col in range(1, row):
            first_num = sequence[row - 1][col - 1]
            second_num = sequence[row - 1][col]
            current_row[col] = first_num + second_num
        sequence.append(current_row)
    return sequence

[print(*x) for x in get_magic_triangle(10)]