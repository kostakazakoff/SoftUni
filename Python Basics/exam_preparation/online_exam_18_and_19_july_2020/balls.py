number_of_balls = int(input())
ball_collor = ''
points = 0
count_red = 0
count_orange = 0
count_yellow = 0
count_white = 0
count_black = 0
count_black = 0
count_others = 0
for i in range(number_of_balls):
    ball_collor = input()
    if ball_collor == 'red':
        points += 5
        count_red += 1
    elif ball_collor == 'orange':
        points += 10
        count_orange += 1
    elif ball_collor == 'yellow':
        points += 15
        count_yellow += 1
    elif ball_collor == 'white':
        points += 20
        count_white += 1
    elif ball_collor == 'black':
        points //= 2
        count_black += 1
    else:
        count_others += 1
print(f'Total points: {points}')
print(f'Red balls: {count_red}')
print(f'Orange balls: {count_orange}')
print(f'Yellow balls: {count_yellow}')
print(f'White balls: {count_white}')
print(f'Other colors picked: {count_others}')
print(f'Divides from black balls: {count_black}')