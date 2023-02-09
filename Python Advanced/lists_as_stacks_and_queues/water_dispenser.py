from collections import deque

quantity = int(input())

command = input()
q = deque()

while command != 'Start':
    q.append(command)
    command = input()

command = input()
while command != 'End':
    if command.startswith('refill'):
        liters = int(command.split()[1])
        quantity += liters
    else:
        liters = int(command)
        if quantity >= liters:
            print(f'{q.popleft()} got water')
            quantity -= liters
        else:
            print(f'{q.popleft()} must wait')
    command = input()

print(f'{quantity} liters left')
