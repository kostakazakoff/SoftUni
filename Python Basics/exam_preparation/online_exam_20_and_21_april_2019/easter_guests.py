import math
guests = int(input())
budget = int(input())
eggs = guests * 2
easter_breads = math.ceil(guests / 3)
price = eggs * 0.45 + easter_breads * 4
diff = abs(budget - price)
if price <= budget:
    print(f'Lyubo bought {easter_breads} Easter bread and {eggs} eggs.')
    print(f'He has {diff:.2f} lv. left.')
else:
    print(f'Lyubo doesn\'t have enough money.')
    print(f'He needs {diff:.2f} lv. more.')