import re


def extract_info(string: str):
    ######## re.compile се използва само веднъж и се изтрива от паметта ###########################
    pattern = re.compile(r'([#\|])(?P<item_name>[A-Za-z ]+)\1(?P<exp_date>\d{2}/\d{2}/\d{2})\1(?P<nutrition>\d{1,5})\1')
    foods = re.finditer(pattern, string)
    return foods


food_str = input()
food_groups = extract_info(food_str)
total_calories = 0
foods_list = []

for group in food_groups:
    total_calories += int(group['nutrition'])
    foods_list.append({'Item': group['item_name'], 'Expire date': group['exp_date'], 'Nutrition': group['nutrition']})


print(f'You have food to last you for: {total_calories // 2000} days!')
[print(f"Item: {x['Item']}, Best before: {x['Expire date']}, Nutrition: {x['Nutrition']}") for x in foods_list]
