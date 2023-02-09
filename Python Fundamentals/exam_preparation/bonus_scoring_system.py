import math

number_of_students, lectures, additional_bonus = int(input()), int(input()), int(input())
bonuses = {0: 0}
for _ in range(number_of_students):
    if lectures == 0:
        break
    attendances = int(input())
    bonuses.update({attendances / lectures * (5 + additional_bonus): attendances})
max_bonus = max(bonuses, key=bonuses.get)
print(f'Max Bonus: {math.ceil(max_bonus)}.')
print(f'The student has attended {bonuses[max_bonus]} lectures.')
