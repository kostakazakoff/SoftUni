championship_level = input()
ticket_type = input()
tickets = int(input())
photos = input()
price = 0

if championship_level == 'Quarter final':
    if ticket_type == 'Standard':
        price = 55.50
    elif ticket_type == 'Premium':
        price = 105.20
    elif ticket_type == 'VIP':
        price = 118.90
elif championship_level == 'Semi final':
    if ticket_type == 'Standard':
        price = 75.88
    elif ticket_type == 'Premium':
        price = 125.22
    elif ticket_type == 'VIP':
        price = 300.40
elif championship_level == 'Final':
    if ticket_type == 'Standard':
        price = 110.10
    elif ticket_type == 'Premium':
        price = 160.66
    elif ticket_type == 'VIP':
        price = 400
price *= tickets

if price > 4000:
    photos = 'N'
    price *= 0.75
elif price > 2500:
    price *= 0.9
if photos == 'Y':
    price += tickets * 40

print(f'{price:.2f}')