fires = input().split('#')
water = int(input())
cell = []
cells = []
effort = 0
total_fire = 0

for fire in fires:
    cell = fire.split(' = ')
    cell_filter = (
        (cell[0] == 'High' and 80 < int(cell[1]) < 126),
        (cell[0] == 'Medium' and 50 < int(cell[1]) < 81),
        (cell[0] == 'Low' and 0 < int(cell[1]) < 51)
    )
    if any(cell_filter):
        cells.append(int(cell[1]))

print('Cells:')

for value in cells:
    if water >= value:
        water -= value
        effort += value * 0.25
        total_fire += value
        print(f' - {value}')

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')
