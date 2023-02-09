from collections import defaultdict


def link_to_side(force_sides: dict, username: str, force: str):
    if not username_in(force_sides, username):
        force_sides[force].append(username)
    return force_sides


def change_side(force_sides: dict, username: str, force: str):
    print(f'{username} joins the {force} side!')
    for k, v in force_sides.items():
        if k != force and username in v:
            v.remove(username)
    force_sides[force].append(username)
    return force_sides


def username_in(force_sides: dict, username: str):
    for names in force_sides.values():
        if username in names:
            return True
    return False


def output(force_sides: dict):
    for k, v in force_sides.items():
        if len(v) > 0:
            print(f'Side: {k}, Members: {len(v)}')
            for username in v:
                print(f'! {username}')


forces = defaultdict(list)
command = input()

while command != 'Lumpawaroo':

    if ' | ' in command:
        command = command.split(' | ')
        side = command[0]
        name = command[1]
        forces = link_to_side(forces, name, side)

    elif ' -> ' in command:
        command = command.split(' -> ')
        side = command[1]
        name = command[0]
        forces = change_side(forces, name, side)

    command = input()

output(forces)