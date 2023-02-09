from os import path


have_to_replace = ("-", ",", ".", "!", "?")

file_path = path.join('.', 'file_handling', 'text_files')
source_file = 'text.txt'

with open(path.join(file_path, source_file), 'r') as file:
    lines = file.readlines()

for i, line in enumerate(lines):
    if i % 2 != 0:
        continue

    for symbol in have_to_replace:
        line = line.replace(symbol, '@')

    print(' '.join(reversed(line.split())))