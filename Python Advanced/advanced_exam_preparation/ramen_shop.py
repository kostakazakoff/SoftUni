from collections import deque


bouls_of_ramen = [int(x) for x in input().split(', ')]
customers = deque([int(x) for x in input().split(', ')])

while bouls_of_ramen and customers:
    if bouls_of_ramen[-1] == customers[0]:
        bouls_of_ramen.pop()
        customers.popleft()
    elif bouls_of_ramen[-1] > customers[0]:
        bouls_of_ramen[-1] -= customers[0]
        customers.popleft()
    else:
        customers[0] -= bouls_of_ramen[-1]
        bouls_of_ramen.pop()

if not customers:
    print('Great job! You served all the customers.')
    if bouls_of_ramen:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in bouls_of_ramen)}")
elif not bouls_of_ramen:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")