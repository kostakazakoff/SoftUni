target_profit = int(input())
service = input()
profit = 0
while service != 'closed':
    if service == 'haircut':
        haircut_type = input()
        if haircut_type == 'mens':
            profit += 15
        elif haircut_type == 'ladies':
            profit += 20
        elif haircut_type == 'kids':
            profit += 10
    elif service == 'color':
        color_type = input()
        if color_type == 'touch up':
            profit += 20
        elif color_type == 'full color':
            profit += 30
    if profit >= target_profit:
        break
    service = input()
diff = target_profit - profit
if profit >= target_profit:
    print('You have reached your target for the day!')
else:
    print(f'Target not reached! You need {diff}lv. more.')
print(f'Earned money: {profit}lv.')