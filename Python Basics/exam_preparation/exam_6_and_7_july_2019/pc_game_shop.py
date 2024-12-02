number_of_sales = int(input())
hearthstone_count = 0
fortnite_count = 0
overwatch_count = 0
others_count = 0
hearthstone_percent = 0
fortnite_percent = 0
overwatch_percent = 0
others_percent = 0

for i in range(1, number_of_sales + 1):
    name_of_the_game = input()
    if name_of_the_game == 'Hearthstone':
        hearthstone_count += 1
    elif name_of_the_game == 'Fornite':
        fortnite_count += 1
    elif name_of_the_game == 'Overwatch':
        overwatch_count += 1
    else:
        others_count += 1

hearthstone_percent = hearthstone_count * 100 / number_of_sales
fortnite_percent = fortnite_count * 100 / number_of_sales
overwatch_percent = overwatch_count * 100 / number_of_sales
others_percent = others_count * 100 / number_of_sales

print(f'Hearthstone - {hearthstone_percent:.2f}%')
print(f'Fornite - {fortnite_percent:.2f}%')
print(f'Overwatch - {overwatch_percent:.2f}%')
print(f'Others - {others_percent:.2f}%')