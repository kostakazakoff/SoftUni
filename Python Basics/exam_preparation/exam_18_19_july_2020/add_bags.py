cena_bagaj_nad_20 = float(input())
kg = float(input())
days_to_trip = int(input())
number_of_bags = int(input())
price = 0
if kg < 10:
    price = 0.2 * cena_bagaj_nad_20
elif kg <= 20:
    price = 0.5 * cena_bagaj_nad_20
else:
    price = cena_bagaj_nad_20
if days_to_trip < 7:
    price *= 1.4
elif days_to_trip <= 30:
    price *= 1.15
else:
    price *= 1.1
price *= number_of_bags
print(f'The total price of bags is: {price:.2f} lv.')