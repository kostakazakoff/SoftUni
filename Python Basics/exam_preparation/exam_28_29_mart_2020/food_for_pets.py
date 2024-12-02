days = int(input())
total_quantity_of_food = float(input())
count_day = 0
dog_eats = 0
cat_eats = 0
bisquits = 0
total_dog_eated_food = 0
total_cat_eated_food = 0
for i in range(1, days + 1):
    count_day += 1
    dog_eats = int(input())
    cat_eats = int(input())
    food_per_day = dog_eats + cat_eats
    if count_day % 3 == 0:
        bisquits += food_per_day * 0.1
    total_dog_eated_food += dog_eats
    total_cat_eated_food += cat_eats
bisquits = round(bisquits)
total_eated_food = total_dog_eated_food + total_cat_eated_food
percent_of_all_food = total_eated_food * 100 / total_quantity_of_food
percent_dog_eated = total_dog_eated_food * 100 / total_eated_food
percent_cat_eated = total_cat_eated_food * 100 / total_eated_food
print(f'Total eaten biscuits: {bisquits}gr.')
print(f'{percent_of_all_food:.2f}% of the food has been eaten.')
print(f'{percent_dog_eated:.2f}% eaten from the dog.')
print(f'{percent_cat_eated:.2f}% eaten from the cat.')

# На конзолата да се отпечатват четири реда:
# "Total eaten biscuits: {количество изядени бисквитки}gr."
# "{процент изядена храна}% of the food has been eaten."
# "{процент изядена храна от кучето}% eaten from the dog."
# "{процент изядена храна от котката}% eaten from the cat."
