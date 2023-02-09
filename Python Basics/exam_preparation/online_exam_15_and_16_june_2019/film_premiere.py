name_of_the_movie = input()
package = input()
tickets = int(input())
price = 0

if name_of_the_movie == 'John Wick':
    if package == 'Drink':
        price = 12
    elif package == 'Popcorn':
        price = 15
    elif package == 'Menu':
        price = 19
elif name_of_the_movie == 'Star Wars':
    if package == 'Drink':
        price = 18
    elif package == 'Popcorn':
        price = 25
    elif package == 'Menu':
        price = 30
    if tickets >= 4:
        price *= 0.7
elif name_of_the_movie == 'Jumanji':
    if package == 'Drink':
        price = 9
    elif package == 'Popcorn':
        price = 11
    elif package == 'Menu':
        price = 14
    if tickets == 2:
        price *= 0.85
price *= tickets

print(f'Your bill is {price:.2f} leva.')