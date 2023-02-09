budget = float(input())
command = input()
product = ''
count = 0
price = 0
total = 0
not_enough_money = False

while command != 'Stop':
    count += 1
    product = command
    price = float(input())
    if count % 3 == 0:
        price /= 2
    if price > budget:
        not_enough_money = True
        count -= 1
        break
    budget -= price
    total += price
    command = input()

diff = price - budget
if not_enough_money:
    print("You don't have enough money!")
    print(f'You need {diff:.2f} leva!')
else:
    print(f'You bought {count} products for {total:.2f} leva.')
