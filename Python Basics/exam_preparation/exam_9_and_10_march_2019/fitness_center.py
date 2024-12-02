number_of_visitors = int(input())
back = 0
chest = 0
legs = 0
abs = 0
protein_shake = 0
protein_bar = 0
protein = 0
all_visitors = 0
for visitors in range(number_of_visitors):
    type_of_service = input()
    if type_of_service == 'Back':
        back += 1
    elif type_of_service == 'Chest':
        chest += 1
    elif type_of_service == 'Legs':
        legs += 1
    elif type_of_service == 'Abs':
        abs += 1
    elif type_of_service == 'Protein shake':
        protein += 1
        protein_shake += 1
    elif type_of_service == 'Protein bar':
        protein += 1
        protein_bar += 1
    all_visitors += 1
train = all_visitors - protein
percent_train = train / all_visitors * 100
percent_protein = protein / all_visitors * 100
print(f'{back} - back')
print(f'{chest} - chest')
print(f'{legs} - legs')
print(f'{abs} - abs')
print(f'{protein_shake} - protein shake')
print(f'{protein_bar} - protein bar')
print(f'{percent_train:.2f}% - work out')
print(f'{percent_protein:.2f}% - protein')