days = int(input())
hours = int(input())
tax = 0
total = 0
for day in range(1, days + 1):
    tax_per_day, tax = 0, 0
    for hour in range(1, hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            tax += 2.5
        elif day % 2 != 0 and hour % 2 == 0:
            tax += 1.25
        else:
            tax += 1
    tax_per_day += tax
    total += tax_per_day
    print(f'Day: {day} - {tax_per_day:.2f} leva')
print(f'Total: {total:.2f} leva')