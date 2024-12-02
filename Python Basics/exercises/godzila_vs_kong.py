budget = float(input())
super = int(input())
super_dress_for_one = float(input())

super_dress = super * super_dress_for_one
decor_price = budget * 10 / 100

if super > 150:
    super_dress = super_dress - super_dress * 10 / 100

costs = super_dress + decor_price
difference = abs(budget - costs)

if costs > budget:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")