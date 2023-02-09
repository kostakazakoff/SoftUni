plunger_days = int(input())
plunger_for_day = int(input())
expected = int(input())
plunger = 0

for day in range(1, plunger_days + 1):
    plunger += plunger_for_day
    if day % 3 == 0:
        plunger += plunger_for_day * 0.5
    if day % 5 == 0:
        plunger -= plunger * 0.3

if plunger >= expected:
    print(f'Ahoy! {plunger:.2f} plunder gained.')
else:
    percentage = plunger * 100 / expected
    print(f'Collected only {percentage:.2f}% of the plunder.')
