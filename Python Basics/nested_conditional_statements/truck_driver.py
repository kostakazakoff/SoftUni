season = input()
drive_distance = float(input())

if drive_distance <= 5000:
    if season == 'Spring' or season == 'Autumn':
        payment_per_km = 0.75
    elif season == 'Summer':
        payment_per_km = 0.9
    elif season == 'Winter':
        payment_per_km = 1.05
elif drive_distance <= 10000:
    if season == 'Spring' or season == 'Autumn':
        payment_per_km = 0.95
    elif season == 'Summer':
        payment_per_km = 1.1
    elif season == 'Winter':
        payment_per_km = 1.25
elif drive_distance <= 20000:
    payment_per_km = 1.45
salary = drive_distance * payment_per_km * 4
salary -= salary * 0.1

print(f'{salary:.2f}')