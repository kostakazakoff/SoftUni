import re

demons = input()
demons = re.split(r' *, *', demons)
result = {}

for demon in demons:
    health_symbols = re.findall(r'[^\d\+\-\*\/\.]', demon)
    damage_symbols = re.findall(r'(\-?)(\d*\.?\d+)', demon)
    operators = ''.join(re.findall(r'[\*\/]', demon))

    health = sum([ord(s) for s in health_symbols])
    damage = sum([eval(f'{x[0]}{float(x[1])}') for x in damage_symbols])

    if operators:
        for operator in operators:
            damage = eval(f'{damage}{operator}2')

    result.update({demon: {'Health': health, 'Damage': damage}})

[print(f'{demon} - {v["Health"]} health, {v["Damage"]:.2f} damage') for demon, v in sorted(result.items())]
