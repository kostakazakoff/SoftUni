money = float(input())
deadline_year = int(input())

for years in range(1800, deadline_year + 1):
    if years % 2 == 0:
        money -= 12000
    else:
        money -= 12000 + 50 * (18 + years - 1800)
if money >=0:
    print(f'Yes! He will live a carefree life and will have {money:.2f} dollars left.')
else:
    money = abs(money)
    print(f'He will need {money:.2f} dollars to survive.')