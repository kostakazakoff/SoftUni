number_of_trekker_groups = int(input())
peak = ''
musala_trekkers = 0
montblanc_trekkers = 0
kilimanjaro_trekkers = 0
k2_trekkers = 0
everest_trekkers = 0
all_trekkers = 0
for i in range(number_of_trekker_groups):
    number_of_trekkers = int(input())
    if number_of_trekkers <= 5:
        peak = 'Musala'
        musala_trekkers += number_of_trekkers
    elif number_of_trekkers <= 12:
        peak = 'Mont Blanc'
        montblanc_trekkers += number_of_trekkers
    elif number_of_trekkers <= 25:
        peak = 'Kilimanjaro'
        kilimanjaro_trekkers += number_of_trekkers
    elif number_of_trekkers <= 40:
        peak = 'К2'
        k2_trekkers += number_of_trekkers
    else:
        peak = 'Everest'
        everest_trekkers += number_of_trekkers
    all_trekkers += number_of_trekkers
p_musala = musala_trekkers * 100 / all_trekkers
p_montblanc = montblanc_trekkers * 100 / all_trekkers
p_kilimanjaro = kilimanjaro_trekkers * 100 / all_trekkers
p_k2 = k2_trekkers * 100 / all_trekkers
p_everest = everest_trekkers * 100 / all_trekkers
print(f'{p_musala:.2f}%')
print(f'{p_montblanc:.2f}%')
print(f'{p_kilimanjaro:.2f}%')
print(f'{p_k2:.2f}%')
print(f'{p_everest:.2f}%')
