period = int(input())
doctors = 7
treated = 0
untreated = 0
all_patients = 0
count_treated_2_days = 0
count_patients_2_days = 0
all_treated = 0
for i in range(1, period + 1):
    patients = int(input())
    all_patients += patients
    if patients <= doctors:
        treated = patients
    else:
        treated = doctors
    all_treated += treated
    count_treated_2_days += treated
    count_patients_2_days += patients
    if i % 2 == 0:
        if count_treated_2_days < count_patients_2_days:
            doctors += 1
        count_treated_2_days = 0
        count_patients_2_days = 0
untreated = all_patients - all_treated
print(f'Treated patients: {all_treated}.')
print(f'Untreated patients: {untreated}.')