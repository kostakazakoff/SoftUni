def sort_by_physic_len(kv):
    sort_by_physic = max(kv[1].values())
    sort_by_len = len(kv[1])
    return sort_by_physic, sort_by_len


command = input()
dwarfs = {}

while command != 'Once upon a time':
    name, color, physic = command.split(' <:> ')
    if color not in dwarfs:
        dwarfs.update({color: {name: int(physic)}})
    elif name not in dwarfs[color]:
        dwarfs[color].update({name: int(physic)})
    elif int(physic) > dwarfs[color][name]:
        dwarfs[color][name] = int(physic)
    command = input()
sorted_dict = sorted(dwarfs.items(), reverse=True, key=sort_by_physic_len)
print(sorted_dict)
dwarfs = {k: v for k, v in sorted(dwarfs.items(), reverse=True, key=sort_by_physic_len)}

for dwarf_hat_color, content in dwarfs.items():
    for dwarf_name, dwarf_physics in content.items():
        print(f'({dwarf_hat_color}) {dwarf_name} <-> {dwarf_physics}')
