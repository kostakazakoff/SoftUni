quantity = int(input())
days = int(input())

# entering the decoration prices and variables:
ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15
day_counter = 0
christmas_spirit = 0
total_cost = 0

# creating a loop, counting days to deadline:
while day_counter != days:
    day_counter += 1
    # defining a tenth_day bool (needed at the end of loop) and reset it to False on every loop:
    it_is_tenth_day = False
    # At the first, checking if the day is 11th (to make a quantity correction):
    if day_counter % 11 == 0:
        quantity += 2
    # Shopping (using only "if" because the day can be in each of the following checks at once):
    if day_counter % 2 == 0:
        total_cost += ornament_set * quantity
        christmas_spirit += 5
    if day_counter % 3 == 0:
        total_cost += (tree_skirt + tree_garlands) * quantity
        christmas_spirit += 13
    if day_counter % 5 == 0:
        total_cost += tree_lights * quantity
        christmas_spirit += 17
        if day_counter % 3 == 0:
            christmas_spirit += 30
    # if the day is 10th, changing the value of it_is_tenth_day bool to True.
    # If it's the last day in loop, we need it:
    if day_counter % 10 == 0:
        it_is_tenth_day = True
        total_cost += tree_skirt + tree_garlands + tree_lights
        christmas_spirit -= 20

# Using the it_is_tenth_day bool:
if it_is_tenth_day:
    christmas_spirit -= 30

# Printing the results:
print(f'Total cost: {total_cost}')
print(f'Total spirit: {christmas_spirit}')