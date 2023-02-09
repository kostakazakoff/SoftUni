def move_to(direct: str):
    global rover_r, rover_c, SIZE
    if direct == 'up': rover_r -= 1
    elif direct == 'down': rover_r += 1
    elif direct == 'left': rover_c -= 1
    elif direct == 'right': rover_c += 1
    rover_r, rover_c = rover_r % SIZE, rover_c % SIZE


SIZE = 6
field = []
for row in range(SIZE):
    line = input().split()
    if 'E' in line: rover_r, rover_c = row, line.index('E')
    field.append(line)
directions = input().split(', ')
water_deposits, metal_deposits, concrete_deposits = 0, 0, 0

for direction in directions:
    move_to(direction)
    if field[rover_r][rover_c] == 'R':
        print(f"Rover got broken at ({rover_r}, {rover_c})")
        break
    elif field[rover_r][rover_c] == 'W':
        print(f'Water deposit found at ({rover_r}, {rover_c})')
        water_deposits += 1
    elif field[rover_r][rover_c] == 'M':
        print(f'Metal deposit found at ({rover_r}, {rover_c})')
        metal_deposits += 1
    elif field[rover_r][rover_c] == 'C':
        print(f'Concrete deposit found at ({rover_r}, {rover_c})')
        concrete_deposits += 1

suitable_area = all((water_deposits, metal_deposits, concrete_deposits))
if suitable_area: print("Area suitable to start the colony.")
else: print("Area not suitable to start the colony.")