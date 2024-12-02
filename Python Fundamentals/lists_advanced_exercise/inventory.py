items = input().split(', ')
command = input()


def inventory(operation, assortment):
    operation = operation.split(' - ')
    action = operation[0]
    item = operation[1]
    new_item = ''

    if ':' in item:
        item = item.split(':')
        new_item = item[1]
        item = item[0]
    # Checking if the item exist in list if so, we can execute 3 of the operations:
    if item in assortment:
        # Defining the item position in list for using it in the following operations:
        item_position = items.index(item)
        # Operation "Drop" - removing the item with specified value from the list:
        if action == 'Drop':
            assortment.remove(item)
        # Operation "Combine Items" - appending the new item after the existing one with the specified position:
        elif action == 'Combine Items':
            assortment.insert(item_position + 1, new_item)
        # Operation "Renew" - replacing the existing item by appending the new one in the end of the list:
        elif action == 'Renew':
            assortment.remove(item)
            assortment.append(item)
    # Item is not in the list, so "Collect" operation can be done:
    else:
        # Operation "Collect" - just append the new item in the end of the list:
        if action == 'Collect':
            assortment.append(item)
    return assortment


while command != 'Craft!':
    inventory(command, items)
    command = input()

print(', '.join(items))
