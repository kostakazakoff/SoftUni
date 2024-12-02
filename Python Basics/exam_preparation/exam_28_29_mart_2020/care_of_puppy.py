food = int(input())
food *= 1000
command = input()
while command != 'Adopted':
    puppy_eats_a_day = int(command)
    food -= puppy_eats_a_day
    command = input()
if food >= 0:
    print(f'Food is enough! Leftovers: {food} grams.')
else:
    print(f'Food is not enough. You need {abs(food)} grams more.')