def shopping_list(*budget, **products):
    budget = budget[0]
    enough = False
    if budget < 100: return 'You do not have enough budget.'
    bought = {}
    for used in range(5):
        if enough: break
        for prod, amount in products.items():
            price = amount[0] * amount[1]
            if price < budget:
                budget -= price
                bought.update({prod: price})
            if len(bought) == 5:
                enough = True
                break
    return '\n'.join([f"You bought {prod} for {price:.2f} leva." for prod, price in bought.items()])
                
     


print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))