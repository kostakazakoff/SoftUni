import re


def extract_emojis_and_numbers():
    global string
    emojis_in_string = re.finditer(r'::[A-Z][a-z]{2,}::|\*{2}[A-Z][a-z]{2,}\*{2}', string)
    emojis_matches = [x.group() for x in emojis_in_string]
    numbers_matches = re.findall(r'\d', string)
    return emojis_matches, numbers_matches


def multiply(numbers_list):
    result = 1
    nums = [int(x) for x in numbers_list]
    for n in nums:
        result *= n
    return result


string = input()
cool_emojis = []

emojis, numbers = extract_emojis_and_numbers()
cool = multiply(numbers)

for emoji in emojis:
    emoji_sum = sum([ord(x) for x in emoji[2:-2]])
    if emoji_sum >= cool:
        cool_emojis.append(emoji)

print(f'Cool threshold: {cool}')
print(f'{len(emojis)} emojis found in the text. The cool ones are:')
[print(emoji) for emoji in cool_emojis]
