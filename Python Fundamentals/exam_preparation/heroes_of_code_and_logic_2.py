def cast_spell(hero_name: str, mp_needed: int, spell_name: str):
    global heroes
    if heroes[hero_name][MP] < mp_needed:
        print(f'{hero_name} does not have enough MP to cast {spell_name}!')
        return
    heroes[hero_name][MP] -= mp_needed
    print(f'{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name][MP]} MP!')


def take_damage(hero_name: str, the_damage: int, the_attacker: str):
    global heroes
    heroes[hero_name][HP] -= the_damage
    if heroes[hero_name][HP] > 0:
        print(f'{hero_name} was hit for {the_damage} HP by {the_attacker} and now has {heroes[hero_name][HP]} HP left!')
        return
    del heroes[hero_name]
    print(f'{hero_name} has been killed by {the_attacker}!')


def recharge_heal(hero_name: str, the_amount: int):
    global heroes
    points_type = MP if action == 'Recharge' else HP
    max_value = 200 if points_type == MP else 100
    current = heroes[hero_name][points_type]
    heroes[hero_name][points_type] += the_amount
    if heroes[hero_name][points_type] > max_value:
        heroes[hero_name][points_type] = max_value
        the_amount = max_value - current
    if points_type == MP:
        print(f'{hero_name} recharged for {the_amount} MP!')
    else:
        print(f'{hero_name} healed for {the_amount} HP!')


heroes_count = int(input())
HP = 'Hit points'
MP = 'Mana points'
heroes = {}

for _ in range(heroes_count):
    name, h_points, m_points = [int(x) if x.isdigit() else x for x in input().split()]
    heroes.update({name: {HP: h_points, MP: m_points}})

command = input()
actions = {'CastSpell': cast_spell, 'TakeDamage': take_damage, 'Recharge': recharge_heal, 'Heal': recharge_heal}

while command != 'End':
    action,  *args = command.split(' - ')
    args = [int(x) if x.isdigit() else x for x in args]
    actions[action](*args)

    command = input()

[print(f'{name}\nHP: {info[HP]}\nMP: {info[MP]}') for name, info in heroes.items()]
