def find_path(row, col, matrix, path, direction):
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
        return
    
    if matrix[row][col] == '*' or matrix[row][col] == 'v':
        return
    
    path.append(direction)

    if matrix[row][col] == 'e':
        print(''.join(path))
    else:    
        matrix[row][col] = 'v'
        find_path(row, col - 1, matrix, path, 'L')
        find_path(row, col + 1, matrix, path, 'R')
        find_path(row - 1, col, matrix, path, 'U')
        find_path(row + 1, col, matrix, path, 'D')
        matrix[row][col] = '-'

    path.pop()


rows = int(input())
cols = int(input())
matrix = [list(input()) for _ in range(rows)]

find_path(0, 0, matrix, [], '')