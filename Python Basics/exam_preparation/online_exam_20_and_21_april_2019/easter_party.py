guests = int(input())
coupon_price = float(input())
budget = float(input())
cake_price = 0.1 * budget
if guests > 20:
    coupon_price *= 0.75
elif guests > 15:
    coupon_price *= 0.8
elif guests >= 10:
    coupon_price *= 0.85
total_price = coupon_price * guests + cake_price
diff = abs(budget - total_price)
if total_price <= budget:
    print(f'It is party time! {diff:.2f} leva left.')
else:
    print(f'No party! {diff:.2f} leva needed.')