entry = input()


def car(position, indexes):
    all_indexes = list(map(int, indexes.split()))
    time = 0
    if position == 'right':
        all_indexes.reverse()
    trace = all_indexes[:len(all_indexes) // 2]
    for times in trace:
        time = time + times if times != 0 else time * 0.8
    return time


left_car_time = car('left', entry)
right_car_time = car('right', entry)

if left_car_time < right_car_time:
    winner = 'left'
    winner_time = f'{left_car_time:.1f}'
else:
    winner = 'right'
    winner_time = f'{right_car_time:.1f}'

print(f'The winner is {winner} with total time: {winner_time}')
