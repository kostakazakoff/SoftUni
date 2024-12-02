import math

racket_price = float(input())
rackets = int(input())
shoes = int(input())
shoes_price = racket_price / 6
price = racket_price * rackets + shoes_price * shoes
equipment_price = price * 0.2
total = price + equipment_price

jocovic_payment = total // 8
sponsor_payment = total * 7 / 8

print(f'Price to be paid by Djokovic {math.floor(jocovic_payment)}')
print(f'Price to be paid by sponsors {math.ceil(sponsor_payment)}')