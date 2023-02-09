destination = input()
money_plus = 0

while destination != 'End':
    needed_budget = float(input())
    saved_money = 0

    while saved_money < needed_budget:
        money_plus = float(input())
        saved_money += money_plus

    print(f'Going to {destination}!')
    destination = input()