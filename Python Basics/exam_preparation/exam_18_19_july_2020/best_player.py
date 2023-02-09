name_of_the_player = ''
top_goals = 0
top_player = ''
hattrick = False
while top_goals < 10:
    name_of_the_player = input()
    if name_of_the_player == 'END':
        break
    else:
        goals = int(input())
    if goals > top_goals:
        top_player = name_of_the_player
        top_goals = goals
    else:
        continue
    if goals >= 3:
        hattrick = True
print(f'{top_player} is the best player!')
if hattrick:
    print(f'He has scored {top_goals} goals and made a hat-trick !!!')
else:
    print(f'He has scored {top_goals} goals.')

