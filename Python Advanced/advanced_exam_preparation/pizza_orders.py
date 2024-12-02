from collections import deque


orders = deque([int(x) for x in input().split(', ')])
employees = [int(x) for x in input().split(', ')]
pizzas_made = 0

while orders and employees:
    if not 0 < orders[0] <= 10:
        orders.popleft()
        continue
    if orders[0] > employees[-1]:
        pizzas = employees.pop()
        orders[0] -= pizzas
        pizzas_made += pizzas
    elif orders[0] <= employees[-1]:
        pizzas_made += orders.popleft()
        employees.pop()

if not orders:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {pizzas_made}')
    print(f'Employees: {", ".join([str(e) for e in employees])}')

else:
    print('Not all orders are completed.')
    print(f'Orders left: {", ".join([str(o) for o in orders])}')
