def register_user(registered_users: dict, user_name: str, number: str):
    if user_name in registered_users.keys():
        print(f'ERROR: already registered with plate number {number}')
        return registered_users
    registered_users[user_name] = number
    print(f'{user_name} registered {number} successfully')
    return registered_users


def unregister(registered_users: dict, user_name: str):
    if user_name not in registered_users.keys():
        print(f'ERROR: user {user_name} not found')
        return registered_users
    registered_users.pop(user_name)
    print(f'{user_name} unregistered successfully')
    return registered_users


def print_registered_users(list_of_registered: dict):
    for key, value in list_of_registered.items():
        print(f'{key} => {value}')


registered = dict()
number_of_commands = int(input())

for _ in range(number_of_commands):
    command = input().split()
    action = command[0]
    user = command[1]
    if action == 'register':
        car_number = command[2]
        registered = register_user(registered, user, car_number)
    else:
        registered = unregister(registered, user)

print_registered_users(registered)