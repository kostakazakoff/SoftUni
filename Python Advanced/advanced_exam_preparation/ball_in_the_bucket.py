def win(the_points: int):
    if 100 <= the_points < 200: return 'Football'
    elif 200 <= the_points < 300: return 'Teddy Bear'
    elif the_points >= 300: return 'Lego Construction Set'


gamefield = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(6)]
points = 0

for _ in range(3):
    r, c = [int(x) for x in eval(input())]

    if not 0 <= r < 6 or not 0 <= c < 6 or gamefield[r][c] != 'B':
        continue

    gamefield[r][c] = 0
    points += sum([gamefield[i][c] for i in range(6)])

prize = win(points)
if prize: print(f"Good job! You scored {points} points, and you've won {prize}.")
else: print(f"Sorry! You need {100 - points} points more to win a prize.")