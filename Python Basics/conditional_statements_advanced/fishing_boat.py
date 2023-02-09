budget = int(input())
season = input()
fishers_number = int(input())
boat_rent_price = 0
discount = 0

if season == 'Spring': boat_rent_price = 3000
elif season == 'Winter': boat_rent_price = 2600
else: boat_rent_price = 4200

if fishers_number <= 6: boat_rent_price *= 0.9
elif fishers_number <= 11: boat_rent_price *= 0.85
else: boat_rent_price *= 0.75

if fishers_number % 2 == 0 and season != 'Autumn': boat_rent_price *= 0.95

difference = abs(budget - boat_rent_price)
if budget >= boat_rent_price:
    print(f'Yes! You have {difference:.2f} leva left.')
else:
    print(f'Not enough money! You need {difference:.2f} leva.')