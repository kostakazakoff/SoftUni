from collections import deque
from functools import total_ordering

miligrams = [int(x) for x in input(). split(', ')]
drinks = deque([int(x) for x in input(). split(', ')])
total_caffeine = 300
stamat_caffeine = 0


while miligrams and drinks:
    mg, drink = miligrams[-1], drinks[0]
    caffeine = mg * drink

    if caffeine > total_caffeine - stamat_caffeine:
        miligrams.pop()
        drinks.append(drinks.popleft())
        stamat_caffeine -= 30
        if stamat_caffeine < 0: stamat_caffeine = 0
        continue

    drinks.popleft()
    miligrams.pop()
    stamat_caffeine += caffeine

if drinks: print(f"Drinks left: {', '.join([str(x) for x in drinks])}")
else: print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {stamat_caffeine} mg caffeine.")