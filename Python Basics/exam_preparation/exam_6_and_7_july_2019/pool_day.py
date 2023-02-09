import math
number_of_guests = int(input())
entry_tax = float(input())
lounge_tax = float(input())
umbrella_tax = float(input())

number_of_umbrellas = math.ceil(number_of_guests / 2)
number_of_lounges = math.ceil(number_of_guests * 0.75)

total = entry_tax * number_of_guests + lounge_tax * number_of_lounges + umbrella_tax * number_of_umbrellas
print(f'{total:.2f} lv.')