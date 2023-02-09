distance = int(input())
day_or_night = input()

taxi_km = 0
bus_km = 0.09
train_km = 0.06
bus_min_distance = 20
train_min_distance = 100
price = 0

if distance >= train_min_distance:
    price = train_km * distance
elif distance >= bus_min_distance:
    price = bus_km * distance
elif day_or_night == 'day':
    price = distance * 0.79 + 0.7
else:
    price = distance * 0.9 + 0.7
print(f"{price:.2f}")