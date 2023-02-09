import re

text = input()
valid_dates = re.findall(r'(\d{2})([\/.-])([A-Z]{1}[a-z]{2})\2(\d{4})', text)
for match in valid_dates:
    print(f'Day: {match[0]}, Month: {match[2]}, Year: {match[3]}')
