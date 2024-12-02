n = int(input())
washmashine_price = float(input())
toy_price = int(input())
money_gift = 0
total_money_gift = 0
toys = 0
for birthday in range(1, n+1):
    if birthday % 2 == 0:
        money_gift += 10
        total_money_gift += money_gift - 1
    else:
        toys += 1
money_for_toys = toys * toy_price
saved_money = money_for_toys + total_money_gift
diff = abs(saved_money - washmashine_price)
if saved_money >= washmashine_price:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')