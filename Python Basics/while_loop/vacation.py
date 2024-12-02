needed_money = float(input())
saved_money = float(input())
days = 0
spend_counter = 0
she_spend_too_much = False
while saved_money < needed_money:
    action = input()
    money_in_action = float(input())
    days += 1
    if action == 'spend':
        spend_counter += 1
        saved_money -=  money_in_action
        if saved_money < 0:
            saved_money = 0
    if spend_counter == 5:
        she_spend_too_much = True
        break
    if action == 'save':
        spend_counter = 0
        saved_money += money_in_action


if she_spend_too_much:
    print("You can't save the money.")
    print(days)
else:
    print(f'You saved the money for {days} days.')