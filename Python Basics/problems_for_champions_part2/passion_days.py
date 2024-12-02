import decimal
budget = decimal.Decimal(input())
command = input()
purchase = 0
purchases_count = 0
while command != 'mall.Enter':
    command = input()

command = input()
while command != 'mall.Exit':
    for sign in command:
        if sign == '*':
            budget += 10
            continue
        purchase = decimal.Decimal(ord(sign))
        if sign.isupper():
            purchase /= 2
        elif sign.islower():
            purchase *= decimal.Decimal(0.3)
        elif sign == '%':
            purchase = budget / 2
        if budget >= purchase > 0:
            budget -= purchase
            purchases_count += 1
    command = input()

if purchases_count == 0:
    print(f'No purchases. Money left: {budget:.2f} lv.')
else:
    print(f'{purchases_count} purchases. Money left: {budget:.2f} lv.')