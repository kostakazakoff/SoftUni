groceries = input().split('!')
command = input()

while command != 'Go Shopping!':
    command = command.split()
    action = command[0]
    item = command[1]

    if item in groceries:
        if action == 'Correct':
            new_item = command[2]
            index = groceries.index(item)
            groceries.insert(index, new_item)
            groceries.remove(item)
        elif action == 'Unnecessary':
            groceries.remove(item)
        elif action == 'Rearrange':
            groceries.append(item)
            groceries.remove(item)

    else:
        if action == 'Urgent':
            groceries.insert(0, item)

    command = input()

output = ', '.join(groceries)
print(output)