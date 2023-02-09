def link_to_force(list_of_users: dict, username: str, force_side: str):
    if username not in list_of_users:
        list_of_users[username] = force_side
        return list_of_users
    return list_of_users


def change_force(list_of_users: dict, username: str, force_side: str):
    list_of_users[username] = force_side
    print(f'{username} joins the {force_side} side!')
    return list_of_users


def output(list_of_users: dict):
    forces = set(list_of_users.values())
    for force in forces:
        force_users = {k: v for k, v in list_of_users.items() if v == force}
        print(f'Side: {force}, Members: {len(force_users)}')
        for name in force_users:
            print(f'! {name}')


users = dict()

command = input()
while command != 'Lumpawaroo':
    if ' | ' in command:
        command = command.split(' | ')
        side = command[0]
        name = command[1]
        users = link_to_force(users, name, side)
    elif ' -> ' in command:
        command = command.split(' -> ')
        side = command[1]
        name = command[0]
        users = change_force(users, name, side)
    command = input()

output(users)