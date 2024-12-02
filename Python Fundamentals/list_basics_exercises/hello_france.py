shopping_list = input().split('|')
budget = float(input())
bought_list = []
total_shopping_price = 0
total_sell_price = 0

for each in shopping_list:
    item_parameters = each.split('->')
    item = item_parameters[0]
    item_price = float(item_parameters[1])
    item_out_of_price = (
        budget < item_price,
        item == 'Clothes' and item_price > 50,
        item == 'Shoes' and item_price > 35,
        item == 'Accessories' and item_price > 20.5
    )
    if any(item_out_of_price):
        continue
    budget -= item_price
    total_shopping_price += item_price
    bought_list.append(item_price)

for price in bought_list:
    sell_price = price * 1.4
    total_sell_price += sell_price
    print(f'{sell_price:.2f}', end=' ')

profit = total_sell_price - total_shopping_price
hello_france = total_sell_price + budget >= 150
print()
print(f'Profit: {profit:.2f}')

if hello_france:
    print('Hello, France!')
else:
    print('Not enough money.')
