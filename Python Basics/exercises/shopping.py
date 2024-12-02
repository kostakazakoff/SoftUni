budget = float(input())
pcs_videocard = int(input())
pcs_cpu = int(input())
pcs_ram = int(input())

videocard_price = 250
videocard_total_price = pcs_videocard * videocard_price
cpu_total_price = videocard_total_price * 0.35 * pcs_cpu
ram_total_price = videocard_total_price * 0.1 * pcs_ram

price = videocard_total_price + cpu_total_price + ram_total_price
if pcs_videocard > pcs_cpu:
    price = price - price * 0.15

difference = abs(budget - price)

if budget >= price:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")