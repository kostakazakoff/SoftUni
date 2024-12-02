from collections import deque


def enough():
    total_fuel = 0
    global petrol, distances
    petrol_copy, distances_copy = petrol.copy(), distances.copy()
    while petrol_copy:
        total_fuel += petrol_copy.popleft()
        distance = distances_copy.popleft()
        if total_fuel < distance:
            return False
        total_fuel -= distance
    return True


number_of_pumps = int(input())
petrol = deque()
distances = deque()
result = 0

for i in range(number_of_pumps):
    load, distance_to_the_next = list(map(int, input().split()))
    petrol.append(load)
    distances.append(distance_to_the_next)

for i in range(number_of_pumps):
    if enough():
        print(i)
        break
    petrol.append(petrol.popleft())
    distances.append(distances.popleft())
