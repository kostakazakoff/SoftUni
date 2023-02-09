command = input()
points = 0
name = ''
max_points = 0
winner = ''

while command != 'Stop':
    name = command
    for i in range(len(name)):
        number = int(input())
        if number == ord(name[i]):
            points += 10
        else:
            points += 2
    if points >= max_points:
        max_points = points
        winner = name
    points = 0
    command = input()

print(f'The winner is {winner} with {max_points} points!')

