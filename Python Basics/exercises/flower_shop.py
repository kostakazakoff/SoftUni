import math

magnolii = int(input())
zumbuli = int(input())
rozi = int(input())
kaktusi = int(input())
gift = float(input())

order = magnolii * 3.25 \
    + zumbuli * 4 \
    + rozi * 3.5 \
    + kaktusi * 8
profit = order - order * 5 / 100
difference = abs(profit - gift)
if profit >= gift:
    print(f'She is left with {math.floor(difference)} leva.')
else:
    print(f'She will have to borrow {math.ceil(difference)} leva.')