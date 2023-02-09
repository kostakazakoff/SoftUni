import re


def extract_info(string: str):
    food_pattern = r'([#|\|])(\b[A-Za-z\s{1}A-Za-z]+\b)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1'
    food = re.findall(food_pattern, string, re.I)
    return food


def output(food_list: list):
    total_calories = sum([int(x[3]) for x in food_list])
    days_left = total_calories // 2000
    print(f'You have food to last you for: {days_left} days!')
    if len(food_list) > 0:
        [print(f'Item: {x[1]}, Best before: {x[2]}, Nutrition: {x[3]}') for x in food_list]


food_str = input()
food_dict = extract_info(food_str)

output(food_dict)