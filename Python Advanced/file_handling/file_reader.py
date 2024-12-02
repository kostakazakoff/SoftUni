from os import path

file_path = path.join('.', 'file_handling', 'text_files', 'numbers.txt')

with open(file_path, 'r') as file:
    lines = file.readlines()
    
result = sum([int(line.strip()) for line in lines])

print(result)
