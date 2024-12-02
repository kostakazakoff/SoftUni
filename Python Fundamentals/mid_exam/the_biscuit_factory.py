employee_for_day_production = int(input())
employees = int(input())
competition_production = int(input())
production_per_month = 0

for day in range(1, 31):
    production_per_day = employees * employee_for_day_production
    if day % 3 == 0:
        production_per_day = (production_per_day * 75) // 100
    production_per_month += production_per_day

percentage = abs(production_per_month * 100 / competition_production - 100)

print(f'You have produced {production_per_month} biscuits for the past month.')
if production_per_month > competition_production:
    print(f'You produce {percentage:.2f} percent more biscuits.')
else:
    print(f'You produce {percentage:.2f} percent less biscuits.')
