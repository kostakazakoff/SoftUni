gambler_1 = input()
gambler_2 = input()
command = input()
points_1 = 0
points_2 = 0
war = False

while command != 'End of game':
    gambler_1_win = False
    gambler_2_win = False
    card_1 = int(command)
    card_2 = int(input())
    if card_1 > card_2:
        points_1 += card_1 - card_2
        gambler_1_win = True
    elif card_2 > card_1:
        points_2 += card_2 - card_1
        gambler_2_win = True
    if war:
        diff = abs(card_1 - card_2)
        break
    if card_1 == card_2:
        war = True
    command = input()

if war:
    print('Number wars!')
    if gambler_1_win:
        print(f'{gambler_1} is winner with {diff} points')
    elif gambler_2_win:
        print(f'{gambler_2} is winner with {diff} points')
else:
    print(f'{gambler_1} has {points_1} points')
    print(f'{gambler_2} has {points_2} points')