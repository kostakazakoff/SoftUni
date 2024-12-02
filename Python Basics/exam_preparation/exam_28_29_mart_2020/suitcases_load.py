load_capacity = float(input())
command = input()
there_is_no_more_space = False
suitcases_loaded = 0
suitcase_volume = 0
while command != 'End':
    suitcase_volume = float(command)
    suitcases_loaded += 1
    if suitcases_loaded % 3 == 0:
        suitcase_volume *= 1.1
    if load_capacity < suitcase_volume:
        suitcases_loaded -= 1
        there_is_no_more_space = True
        break
    load_capacity -= suitcase_volume
    command = input()
if there_is_no_more_space:
    print('No more space!')
else:
    print('Congratulations! All suitcases are loaded!')
print(f'Statistic: {suitcases_loaded} suitcases loaded.')