age = int(input())

menu = {
    'kid': 'drink toddy',
    'teen': 'drink coke',
    'young adult': 'drink beer',
    'adult': 'drink whisky'
}

if age <= 14:
    output = menu['kid']
elif age <= 18:
    output = menu['teen']
elif age <= 21:
    output = menu['young adult']
else:
    output = menu['adult']

print(output)