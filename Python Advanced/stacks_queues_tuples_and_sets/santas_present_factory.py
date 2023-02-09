from collections import deque

materials = [int(mat) for mat in input().split()]
magic_values = deque(int(magic) for magic in input().split())
considered = []

gifts = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}

while materials and magic_values:
    material, magic = materials.pop(), magic_values.popleft()
    result = material * magic

    if result < 0:
        materials.append(material + magic)
        continue

    if material == 0 and magic == 0:
        continue
    if material == 0:
        magic_values.appendleft(magic)
        continue
    if magic == 0:
        materials.append(material)
        continue

    if result in gifts:
        considered.append(gifts[result])
        continue

    materials.append(material + 15)

succeed = (
    'Doll' in considered and 'Wooden train' in considered,
    'Teddy bear' in considered and 'Bicycle' in considered
)

if any(succeed):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    output = []
    while materials:
        output.append(materials.pop())
    print(f"Materials left: {', '.join([str(x) for x in output])}")

if magic_values:
    print(f"Magic left: {', '.join(str(x) for x in magic_values)}")

output = {}
[output.update({x: considered.count(x)}) for x in set(considered)]
[print(f'{key}: {value}') for key, value in sorted(output.items())]
