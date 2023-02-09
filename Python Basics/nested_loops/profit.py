all_coins_1 = int(input())
all_coins_2 = int(input())
all_banknotes_5 = int(input())
sum = int(input())

for coins_1 in range(all_coins_1 + 1):
    for coins_2 in range(all_coins_2 + 1):
        for banknotes_5 in range(all_banknotes_5 + 1):
            if banknotes_5 * 5 + coins_2 * 2 + coins_1 == sum:
                print(f'{coins_1} * 1 lv. + {coins_2} * 2 lv. + {banknotes_5} * 5 lv. = {sum} lv.')