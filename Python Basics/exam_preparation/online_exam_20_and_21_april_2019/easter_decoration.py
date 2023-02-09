clients = int(input())
all_clients_expenses = 0

for client in range(clients):
    client_purchase_counter = 0
    price = 0
    purchase = input()

    while purchase != 'Finish':
        if purchase == 'basket':
            price += 1.5
        elif purchase == 'wreath':
            price += 3.8
        elif purchase == 'chocolate bunny':
            price += 7
        client_purchase_counter += 1
        purchase = input()

    if client_purchase_counter % 2 == 0:
        price *= 0.8
    all_clients_expenses += price
    print(f'You purchased {client_purchase_counter} items for {price:.2f} leva.')
average_expenses = all_clients_expenses / clients
print(f'Average bill per client is: {average_expenses:.2f} leva.')
