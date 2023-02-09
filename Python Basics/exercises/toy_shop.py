puzzle = 2.6
puppet = 3.0
tedy = 4.1
minon = 8.2
truck = 2.0

voyage_price = float(input())
puzzle_pc = int(input())
puppet_pc = int(input())
tedy_pc = int(input())
minon_pc = int(input())
truck_pc = int(input())

puzzle_total_price = puzzle_pc * puzzle
puppet_total_price = puppet_pc * puppet
tedy_total_price = tedy_pc * tedy
minon_total_price = minon_pc * minon
truck_total_price = truck_pc * truck

quantity = puzzle_pc + puppet_pc + tedy_pc + minon_pc + truck_pc
total_price = puzzle_total_price + puppet_total_price + tedy_total_price + minon_total_price + truck_total_price

if quantity >= 50:
    total_price = total_price - total_price * 25 / 100

rent_for_shop = total_price * 10 / 100
profit = total_price - rent_for_shop
difference = abs(voyage_price - profit)

if voyage_price <= profit:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")