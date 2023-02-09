companions = int(input())
days = int(input())
earn = 0
expenses = 0
profit = 0
profit_per_day = 0
coins_per_companion = 0

for day in range(1, days + 1):
    if day % 10 == 0:
        companions -= 2
    if day % 15 == 0:
        companions += 5
    earn = 50
    expenses = 2 * companions
    if day % 3 == 0:
        expenses += 3 * companions
    if day % 5 == 0:
        earn += 20 * companions
        if day % 3 == 0:
            expenses += 2 * companions
    profit_per_day = earn - expenses
    profit += profit_per_day

coins_per_companion = profit // companions
print(f'{companions} companions received {coins_per_companion} coins each.')