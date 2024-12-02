from os import path


file_path = path.join('.', 'file_handling', 'text_files', 'text.txt')

try:
    with open(file_path, 'r') as file:
        print('File Found')
except FileNotFoundError:
    print('File not found')