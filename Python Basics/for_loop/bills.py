months = int(input())
water = 0
net = 0
others = 0
energy = 0
for i in range(months):
    electricity = float(input())
    energy += electricity
    water += 20
    net += 15
    others += (electricity + 20 + 15) * 1.2
average = (energy + water + net + others) / months
print(f'Electricity: {energy:.2f} lv')
print(f'Water: {water:.2f} lv')
print(f'Internet: {net:.2f} lv')
print(f'Other: {others:.2f} lv')
print(f'Average: {average:.2f} lv')