def in_collection(the_item: str):
    if the_item in collection:
        return True
    return False


def collect(the_collection: list, the_item: str):
    if in_collection(the_item):
        return the_collection
    the_collection.append(the_item)
    return the_collection


def drop(the_collection: list, the_item: str):
    if not in_collection(the_item):
        return the_collection
    the_collection = [x for x in the_collection if x != the_item]
    return the_collection


def combine(the_collection: list, the_item: str, the_new_item: str):
    if not in_collection(the_item):
        return the_collection
    index = the_collection.index(the_item)
    the_collection.insert(index + 1, the_new_item)
    return the_collection


def renew(the_collection: list, the_item: str):
    if not in_collection(the_item):
        return the_collection
    index = the_collection.index(the_item)
    the_collection.append(the_collection.pop(index))
    return the_collection


collection = input().split(', ')

command = input()

while command != 'Craft!':
    action, item = command.split(' - ')

    if action == 'Collect':
        collection = collect(collection, item)

    elif action == 'Drop':
        collection = drop(collection, item)

    elif action == 'Combine Items':
        item, new_item = item.split(':')
        collection = combine(collection, item, new_item)

    elif action == 'Renew':
        collection = renew(collection, item)

    command = input()

print(', '.join(collection))
