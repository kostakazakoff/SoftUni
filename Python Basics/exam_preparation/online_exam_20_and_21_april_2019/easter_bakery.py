flour_price = float(input())
flour_kg = float(input())
sugar_kg = float(input())
eggs_packets = int(input())
yeast_pc = int(input())
sugar_price = flour_price * 0.75
eggs_price = flour_price * 1.1
yeast_price = sugar_price * 0.2
price = flour_kg * flour_price + sugar_kg * sugar_price + eggs_packets * eggs_price + yeast_pc * yeast_price
print(f'{price:.2f}')
