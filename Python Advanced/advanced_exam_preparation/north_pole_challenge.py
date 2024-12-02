def step_to(d: str):
    global workshop, r, c
    workshop[r][c] = 'x'
    if d == 'up': r -= 1
    if d == 'down': r += 1
    if d == 'left': c -= 1
    if d == 'right': c += 1
    r, c = r % ROWS, c % COLS


ROWS, COLS = [int(x) for x in input().split(', ')]
decorations, gifts, chrstms_cookies = 0, 0, 0
dec_collected, gifts_collected, cookies_collected = 0, 0, 0
workshop = []
merry_christmas = False

for row in range(ROWS):
    line = input().split()
    if 'Y' in line: r, c = row, line.index('Y')
    if 'D' in line: decorations += line.count('D')
    if 'G' in line: gifts += line.count('G')
    if 'C' in line: chrstms_cookies += line.count('C')
    workshop.append(line)

command = input().split('-')
while command[0] != 'End':
    direction, steps = command[0], int(command[1])

    for _ in range(steps):
        step_to(direction)
        if workshop[r][c] == 'D': dec_collected += 1
        if workshop[r][c] == 'G': gifts_collected += 1
        if workshop[r][c] == 'C': cookies_collected += 1
        workshop[r][c] = 'Y'
        if all((decorations == dec_collected, gifts == gifts_collected, chrstms_cookies == cookies_collected)):
            print('Merry Christmas!')
            merry_christmas = True
            break
    
    if merry_christmas: break

    command = input().split('-')

print("You've collected:")
print(f'- {dec_collected} Christmas decorations')
print(f'- {gifts_collected} Gifts')
print(f'- {cookies_collected} Cookies')
[print(*row) for row in workshop]