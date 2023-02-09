indexes = list(map(int, input().split()))
left = indexes[:(len(indexes) // 2)]
indexes.reverse()
right = indexes[:(len(indexes) // 2)]


def time(position):
    t = 0
    for each in position:
        if each != 0: t += each
        else: t *= 0.8
    return t


left_car_time = time(left)
right_car_time = time(right)

if left_car_time < right_car_time:
    winner = 'left'
    winner_time = f'{left_car_time:.1f}'
else:
    winner = 'right'
    winner_time = f'{right_car_time:.1f}'

print(f'The winner is {winner} with total time: {winner_time}')