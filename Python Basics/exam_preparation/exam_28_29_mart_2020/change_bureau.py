bitcoins = int(input())
juans = float(input())
comission = float(input())

bitcoin_lv = bitcoins * 1168
lv = bitcoins * 1168 + juans * 0.15 * 1.76
eur = lv / 1.95
total = eur - eur * comission / 100
print(f'{total:.2f}')