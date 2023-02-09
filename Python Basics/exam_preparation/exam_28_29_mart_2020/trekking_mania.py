number_of_groups = int(input())
musala_trekkers = 0
montblan_trekkers = 0
kilimanjaro_trekkers = 0
k2_trekkers = 0
everest_trekkers = 0
for i in range(1, number_of_groups + 1):
    number_of_trekkers_in_group = int(input())
    if number_of_trekkers_in_group < 6:
        musala_trekkers += number_of_trekkers_in_group
    elif number_of_trekkers_in_group < 13:
        montblan_trekkers += number_of_trekkers_in_group
    elif number_of_trekkers_in_group < 26:
        kilimanjaro_trekkers += number_of_trekkers_in_group
    elif number_of_trekkers_in_group < 41:
        k2_trekkers += number_of_trekkers_in_group
    else:
        everest_trekkers += number_of_trekkers_in_group
all_treckers = musala_trekkers + montblan_trekkers + kilimanjaro_trekkers + k2_trekkers + everest_trekkers
musala_trekkers *= 100 / all_treckers
montblan_trekkers *= 100 / all_treckers
kilimanjaro_trekkers *= 100 / all_treckers
k2_trekkers *= 100 / all_treckers
everest_trekkers *= 100 / all_treckers
print(f'{musala_trekkers:.2f}%')
print(f'{montblan_trekkers:.2f}%')
print(f'{kilimanjaro_trekkers:.2f}%')
print(f'{k2_trekkers:.2f}%')
print(f'{everest_trekkers:.2f}%')