class Area:
    def __init__(self, row, col, size):
        self.row = row
        self.col = col
        self.size = size


def seek_and_count(r, c, rows, cols, matrix):
    if r < 0 or c < 0 or r >= rows or c >= cols or matrix[r][c] != '-':
        return 0
    
    matrix[r][c] = 'v'
    result = 1
    
    result += seek_and_count(r, c + 1, rows, cols, matrix)
    result += seek_and_count(r, c - 1, rows, cols, matrix)
    result += seek_and_count(r + 1, c, rows, cols, matrix)
    result += seek_and_count(r - 1, c, rows, cols, matrix)

    return result


rows = int(input())
cols = int(input())

matrix = [list(input()) for _ in range(rows)]
areas = []
number_of_areas = 0

for row in range(rows):
    for col in range(cols):
        arr_size = seek_and_count(row, col, rows, cols, matrix)
        if arr_size:
            number_of_areas += 1
            areas.append(Area(row, col, arr_size))

areas = sorted(areas, key=lambda a: -a.size)
print(f'Total areas found: {len(areas)}')
[print(f'Area #{idx+1} at ({area.row}, {area.col}), size: {area.size}') for idx, area in enumerate(areas)]
