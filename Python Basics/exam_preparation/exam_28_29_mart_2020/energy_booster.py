gel_fruit = input()
gel_size = input()
gel_quantity = int(input())
price = 0
if gel_fruit == 'Watermelon':
    if gel_size == 'small':
        price = 112
    elif gel_size == 'big':
        price = 143.5
elif gel_fruit == 'Mango':
    if gel_size == 'small':
        price = 73.32
    elif gel_size == 'big':
        price = 98
elif gel_fruit == 'Pineapple':
    if gel_size == 'small':
        price = 84.2
    elif gel_size == 'big':
        price = 124
elif gel_fruit == 'Raspberry':
    if gel_size == 'small':
        price = 40
    elif gel_size == 'big':
        price = 76
price *= gel_quantity
if price > 1000:
    price /= 2
elif price >= 400:
    price *= 0.85
print(f'{price:.2f} lv.')
