animal = input()

mammal = 'dog'
reptile = 'crocodile, tortoise, snake'

if animal in mammal:
    print('mammal')
elif animal in reptile:
    print('reptile')
else:
    print('unknown')