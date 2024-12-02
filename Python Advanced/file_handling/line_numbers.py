from os import path
from re import findall


file_path = path.join('.', 'file_handling', 'text_files')
source_file = 'text.txt'
destination_file = 'line_numbers.txt'
letters_pattern = r'[A-z]'
marks_pattern = r'[^\s\w]'

with open(path.join(file_path, source_file), 'r') as file:
    lines = file.readlines()

with open(path.join(file_path, destination_file), 'a') as file:
    for i, line in enumerate(lines):
        letters_count = len(findall(letters_pattern, line))
        marks_count = len(findall(marks_pattern, line))
        file.write(f'Line {i + 1}: {line.strip()} ({letters_count})({marks_count})\n')
