from collections import deque


rows, cols = [int(x) for x in input().split()]
snake_queue = deque(list(input()))
matrix = [['' for col in range(cols)] for _ in range(rows)]

for row in range(rows):
    start, end, step = (0, cols, 1) if row % 2 == 0 else (cols - 1, -1, -1)
    for col in range(start, end, step):
        matrix[row][col] = snake_queue[0]
        snake_queue.append(snake_queue.popleft())

[print(''.join(r)) for r in matrix]