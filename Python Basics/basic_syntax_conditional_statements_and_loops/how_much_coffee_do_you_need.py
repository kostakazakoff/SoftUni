command = input()
coffees = 0
options = ['coding', 'dog', 'cat', 'movie']

while command != 'END':
    if command.lower() not in options:
        command = input()
        continue
    if command.islower():
        coffees += 1
    elif command.isupper():
        coffees += 2
    if coffees > 5:
        print('You need extra sleep')
        break
    command = input()
else:
    print(coffees)
