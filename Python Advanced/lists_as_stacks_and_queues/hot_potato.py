from collections import deque

children = input().split()

q = deque()
[q.append(x) for x in children]
step = int(input())

while len(q) > 1:
    toss_count = 0
    [q.append(q.popleft()) for _ in range(step - 1)]
    print(f'Removed {q.popleft()}')

print(f'Last is {q.popleft()}')
