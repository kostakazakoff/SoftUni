budget = float(input())
category = input()
fans = int(input())
transport = 0
discount = 0
if fans > 50:
    discount = 25
elif fans > 24:
    discount = 40
