import math

bakes = int(input())
packs_of_flour = 0
packs_of_sugar = 0
sugar = 0
flour = 0
max_flour = 0
max_sugar = 0
for bake in range(bakes):
    sugar_g = int(input())
    flour_g = int(input())
    sugar += sugar_g
    flour += flour_g
    if sugar_g > max_sugar:
        max_sugar = sugar_g
    if flour_g > max_flour:
        max_flour = flour_g
packs_of_sugar = math.ceil(sugar / 950)
packs_of_flour = math.ceil(flour / 750)
print(f'Sugar: {packs_of_sugar}')
print(f'Flour: {packs_of_flour}')
print(f'Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.')
