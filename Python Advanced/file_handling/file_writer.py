from os import path

file_path = path.join('.', 'file_handling', 'text_files', 'my_first_file.txt')

with open(file_path, 'w') as file:
    file.write('I just created my first file!')