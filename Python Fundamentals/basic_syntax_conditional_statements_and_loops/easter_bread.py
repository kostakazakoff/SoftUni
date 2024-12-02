budget = float(input())
price_flour_kg = float(input())
price_pack_eggs = price_flour_kg * 0.75
price_milk_l = price_flour_kg * 1.25
price_of_bread = price_pack_eggs + price_flour_kg + price_milk_l * 0.25
bread_counter = 0
eggs_counter = 0
while budget >= price_of_bread:
    budget -= price_of_bread
    bread_counter += 1
    eggs_counter += 3
    if bread_counter % 3 == 0:
        eggs_counter -= bread_counter - 2
print(f'You made {bread_counter} loaves of Easter bread! Now you have {eggs_counter} eggs and {budget:.2f}BGN left.')
