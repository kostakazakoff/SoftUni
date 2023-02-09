number_of_eggs = int(input())
red = 0
orange = 0
blue = 0
green = 0
max = 0
max_colour = ''
for egg in range(number_of_eggs):
    colour = input()
    if colour == 'red':
        red += 1
    elif colour == 'orange':
        orange += 1
    elif colour == 'blue':
        blue += 1
    else:
        green += 1
    if red > max:
        max = red
        max_colour = 'red'
    if orange > max:
        max = orange
        max_colour = 'orange'
    if blue > max:
        max = blue
        max_colour = 'blue'
    if green > max:
        max = green
        max_colour = 'green'
print(f'Red eggs: {red}')
print(f'Orange eggs: {orange}')
print(f'Blue eggs: {blue}')
print(f'Green eggs: {green}')
print(f'Max eggs: {max} -> {max_colour}')
