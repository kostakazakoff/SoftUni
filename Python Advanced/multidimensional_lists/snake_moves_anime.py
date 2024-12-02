from collections import deque
from time import sleep
from os import system, name


rows, cols = [int(x) for x in input().split()]
snake_queue = deque(list(input()))
matrix = [['_' for _ in range(cols)] for _ in range(rows)]

system('cls' if name == 'nt' else 'clear')
[print('|'.join(r)) for r in matrix]
sleep(0.02)


for row in range(rows):
    start, end, step = (0, cols, 1) if row % 2 == 0 else (cols - 1, -1, -1)
    for col in range(start, end, step):
        matrix[row][col] = snake_queue[0]
        snake_queue.append(snake_queue.popleft())
        system('cls' if name == 'nt' else 'clear')
        [print('|'.join(r)) for r in matrix]
        sleep(0.02)

