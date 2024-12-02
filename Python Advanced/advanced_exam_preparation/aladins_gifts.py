from collections import deque


def requirements(value):
    if 100 <= value < 200: return 'Gemstone'
    elif value < 300: return 'Porcelain Sculpture'
    elif value < 400: return 'Gold'
    elif value < 500: return 'Diamond Jewellery'


def check_result():
    product = None
    result = mat + magc
    if result < 100:
        if result % 2 == 0: result = mat * 2 + magc * 3
        else: result *= 2
    elif result >= 500: result /= 2
    if 100 <= result < 500: product = requirements(result)
    return product



materials = [int(x) for x in input().split()]
magics = deque([int(x) for x in input().split()])
presents = {
    'Gemstone': 0,
    'Porcelain Sculpture': 0,
    'Gold': 0,
    'Diamond Jewellery': 0
}


while materials and magics:
    mat, magc = materials.pop(), magics.popleft()

    present = check_result()
    if present in presents:
        presents[present] += 1
    
    succeed = (
            (presents['Gemstone'] and presents['Porcelain Sculpture']) or
            (presents['Gold'] and presents['Diamond Jewellery'])
        )

if succeed: print("The wedding presents are made!")
else: print("Aladdin does not have enough wedding presents.")

if materials: print(f"Materials left: {', '.join([str(x) for x in materials])}")
if magics: print(f"Magic left: {', '.join([str(x) for x in magics])}")

[print(f'{present}: {amount}') for present, amount in sorted(presents.items()) if amount]