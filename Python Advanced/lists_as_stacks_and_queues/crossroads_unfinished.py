from collections import deque

green_light_duration, free_window = int(input()), int(input())
pass_time_duration = green_light_duration + free_window
cars_queue = deque()
car_chars = deque()
total_cars_passed = 0
time_count = 0

command = input()
while command != 'END':

    if command != 'green':
        cars_queue.append(command)
        command = input()
        continue

    time_count = 0
    while len(cars_queue) > 0 and time_count < green_light_duration:
        car = cars_queue.popleft()
        [car_chars.append(x) for x in car]

        while len(car_chars) > 0:
            current_char = car_chars.popleft()
            if time_count == pass_time_duration and len(car_chars) > 0:
                print("A crash happened!")
                print(f"{car} was hit at {current_char}.")
                exit()
            time_count += 1
        total_cars_passed += 1

    command = input()

print("Everyone is safe.")
print(f"{total_cars_passed} total cars passed the crossroads.")
