from collections import deque


def seat_match():
    global seat_one, seat_two, seats
    if seat_one in seats: return seat_one
    elif seat_two in seats: return seat_two


seats = [s for s in input().split(', ')]
numbers_left_queue = deque([int(n) for n in input().split(', ')])
numbers_right_queue = deque([int(n) for n in input().split(', ')])
rotations = 0
seat_matches = []

while len(seat_matches) < 3 and rotations < 10:
    first_num, second_num = numbers_left_queue.popleft(), numbers_right_queue.pop()
    seat_one = f'{first_num}{chr(first_num + second_num)}'
    seat_two = f'{second_num}{chr(first_num + second_num)}'

    found = seat_match()

    if found:
        seat_matches.append(found)
        seats.remove(found)
        
    else:
        numbers_left_queue.append(first_num)
        numbers_right_queue.appendleft(second_num)
    
    rotations += 1

print(f"Seat matches: {', '.join(seat_matches)}")
print(f'Rotations count: {rotations}')
