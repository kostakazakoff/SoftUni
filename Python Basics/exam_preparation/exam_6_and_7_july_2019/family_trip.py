budget = float(input())
number_of_overnights = int(input())
overnight_price = float(input())
extra_expenses_percent = int(input())

if number_of_overnights > 7:
    overnight_price *= 0.95
total = number_of_overnights * overnight_price + budget * extra_expenses_percent / 100
diff = abs(budget - total)
if total <= budget:
    print(f'Ivanovi will be left with {diff:.2f} leva after vacation.')
else:
    print(f'{diff:.2f} leva needed.')