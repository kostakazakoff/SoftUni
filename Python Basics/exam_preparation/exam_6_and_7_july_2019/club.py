desired_profit = float(input())
drink_type = input()
profit = 0
diff = 0
total_profit = 0
we_have_the_desired_profit = False

while drink_type != 'Party!':
    number_of_drinks = int(input())
    drink_price = len(drink_type)
    profit = number_of_drinks * drink_price
    if profit % 2 != 0:
        profit *= 0.75
    total_profit += profit
    if total_profit >= desired_profit:
        we_have_the_desired_profit = True
        break
    drink_type = input()

diff = desired_profit - total_profit
if we_have_the_desired_profit:
    print('Target acquired.')
elif drink_type == 'Party!':
    print(f'We need {diff:.2f} leva more.')
print(f'Club income - {total_profit:.2f} leva.')

