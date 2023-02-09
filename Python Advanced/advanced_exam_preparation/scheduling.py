tasks = [[x, int(y)] for x, y in enumerate(input().split(', '))]
tasks = sorted(tasks, key=lambda tasks: tasks[1])
cycles = 0
idx = int(input())

for task in tasks:
    cycles += task[1]
    if task[0] == idx: break

print(cycles)