days = int(input())
hours = int(input())
tax = 0

for d in range(1, days + 1):
    tax_per_day, tax_per_hour = 0, 0
    for h in range(1, hours + 1):
        if d % 2 == 0 and h % 2 != 0: tax_per_hour += 2.5
        elif d % 2 != 0 and h % 2 == 0: tax_per_hour += 1.25
        else: tax_per_hour += 1
    tax_per_day += tax_per_hour
    tax += tax_per_day
    print(f'Day: {d} - {tax_per_day:.2f} leva')
print(f'Total: {tax:.2f} leva')