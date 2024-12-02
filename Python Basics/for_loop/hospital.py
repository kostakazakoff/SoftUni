period = int(input())
doctors = 7
treated = 0
untreated = 0
all_patients = 0

for i in range(1, period + 1):
    patients_for_a_day = int(input())
    if i % 3 == 0:
        if treated < untreated:
            doctors += 1
    if patients_for_a_day <= doctors:
        treated += patients_for_a_day
    else:
        treated += doctors
    all_patients += patients_for_a_day
    untreated = all_patients - treated

print(f'Treated patients: {treated}.')
print(f'Untreated patients: {untreated}.')