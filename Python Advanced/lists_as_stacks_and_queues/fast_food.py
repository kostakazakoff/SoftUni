from collections import deque


def ordering():
    global orders, food_quantity, complete
    while orders:
        if food_quantity >= orders[0]:
            food_quantity -= orders.popleft()
        else:
            complete = False
            break


def report():
    global orders, complete
    if complete:
        print('Orders complete')
    else:
        print(f'Orders left: {" ".join(map(str, orders))}')


food_quantity = int(input())
orders = deque(map(int, input().split()))
complete = True

print(max(orders))

ordering()
report()
