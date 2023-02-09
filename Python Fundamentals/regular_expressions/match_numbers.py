import re

text = input()
valid_nums_pattern = r'(^|(?<=\s))-?([0-9]|[1-9][0-9]+)(\.\d+)?($|(?=\s))'
valid_numbers = re.finditer(valid_nums_pattern, text)
output = ' '.join([x.group() for x in valid_numbers])
print(output)
