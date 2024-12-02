from collections import deque

q = deque()

command = input()

while command != 'End':
    if command == 'Paid':
        [print(name) for name in q]
        q.clear()
    else:
        q.append(command)
    command = input()

print(f'{len(q)} people remaining.')
