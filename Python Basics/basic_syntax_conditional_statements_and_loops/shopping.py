budget = int(input())
purchase = input()

while purchase != 'End':
    purchase = int(purchase)
    enough_money = purchase <= budget
    if not enough_money:
        print('You went in overdraft!')
        break
    budget -= purchase
    purchase = input()

else:
    print('You bought everything needed.')
