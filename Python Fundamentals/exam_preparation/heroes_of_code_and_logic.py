def cast_spell(hero_name: str, mp_needed: int, spell_name: str):
    if heroes[hero_name][MP] < mp_needed:
        print(f'{hero_name} does not have enough MP to cast {spell_name}!')
        return
    heroes[hero_name][MP] -= mp_needed
    print(f'{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name][MP]} MP!')


def take_damage(hero_name: str, the_damage: int, the_attacker: str):
    heroes[hero_name][HP] -= the_damage
    if heroes[hero_name][HP] > 0:
        print(f'{hero_name} was hit for {the_damage} HP by {the_attacker} and now has {heroes[hero_name][HP]} HP left!')
        return
    del heroes[hero_name]
    print(f'{hero_name} has been killed by {the_attacker}!')


def recharge_heal(hero_name: str, the_amount: int, variable: str):
    max_value = 200 if variable == MP else 100
    current = heroes[hero_name][variable]
    heroes[hero_name][variable] += the_amount
    if heroes[hero_name][variable] > max_value:
        heroes[hero_name][variable] = max_value
        the_amount = max_value - current
    if variable == MP:
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

while command != 'End':
    action, name, *info = command.split(' - ')

    if action == 'CastSpell':
        mp, spell = [int(x) if x.isdigit() else x for x in info]
        cast_spell(name, mp, spell)

    elif action == 'TakeDamage':
        damage, attacker = [int(x) if x.isdigit() else x for x in info]
        take_damage(name, damage, attacker)

    elif action == 'Recharge':
        amount = int(info[0])
        recharge_heal(name, amount, MP)

    elif action == 'Heal':
        amount = int(info[0])
        recharge_heal(name, amount, HP)

    command = input()

[print(f'{name}\nHP: {info[HP]}\nMP: {info[MP]}') for name, info in heroes.items()]
