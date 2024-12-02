load_number = int(input())
price = 0
bus_load = 0
truck_load = 0
train_load = 0
total_weight = 0
for i in range(load_number):
    load_weight = int(input())
    if load_weight < 4:
        price += load_weight * 200
        bus_load += load_weight
    elif load_weight < 12:
        price += load_weight * 175
        truck_load += load_weight
    else:
        price += load_weight * 120
        train_load += load_weight
total_weight = bus_load + truck_load + train_load
average_price = price / total_weight
bus_p = bus_load * 100 / total_weight
truck_p = truck_load * 100 / total_weight
train_p = train_load * 100 / total_weight

print(f'{average_price:.2f}')
print(f'{bus_p:.2f}%')
print(f'{truck_p:.2f}%')
print(f'{train_p:.2f}%')