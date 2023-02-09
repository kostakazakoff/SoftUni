def to_do_list_priority(tasks: list):
    return [task[1] for task in sorted(tasks, key=lambda x: int(x[0]))]


command = input()
task_list = []
while command != 'End':
    task_list.append(command.split('-'))
    command = input()

print(to_do_list_priority(task_list))
