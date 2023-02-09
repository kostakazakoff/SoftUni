def have_a_plunder(*args):
    global towns, P, G
    the_town, the_people, the_gold = args
    towns[the_town][P] -= the_people
    towns[the_town][G] -= the_gold
    print(f'{the_town} plundered! {the_gold} gold stolen, {the_people} citizens killed.')
    if towns[the_town][P] == 0 or towns[the_town][G] == 0:
        print(f'{the_town} has been wiped off the map!')
        del towns[the_town]


def have_a_prosper(*args):
    global towns, P, G
    the_town, the_gold = args
    if the_gold < 0:
        print(f'Gold added cannot be a negative number!')
        return
    towns[the_town][G] += the_gold
    print(f'{the_gold} gold added to the city treasury. {the_town} now has {towns[the_town][G]} gold.')


def enter_the_content():
    global command, towns, P, G
    the_town, the_population, the_gold = command
    if the_town not in towns:
        towns[the_town] = {P: the_population, G: the_gold}
        return
    towns[the_town][P] += the_population
    towns[the_town][G] += the_gold


towns = {}
P, G = 'Population', 'Gold'
funcs = {'Plunder': have_a_plunder, 'Prosper': have_a_prosper}
command = input()
while command != 'Sail':
    command = [int(x) if x.isdigit() else x for x in command.split("||")]
    enter_the_content()
    command = input()

command = input()
while command != 'End':
    func, *info = command.split('=>')
    info = [int(x) if x.isdigit() or x[0] == '-' else x for x in info]
    funcs[func](*info)
    command = input()

if len(towns) == 0:
    print('Ahoy, Captain! All targets have been plundered and destroyed!')
else:
    print(f'Ahoy, Captain! There are {len(towns)} wealthy settlements to go to:')
    [print(f'{k} -> Population: {v[P]} citizens, Gold: {v[G]} kg') for k, v in towns.items()]