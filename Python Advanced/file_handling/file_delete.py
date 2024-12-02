from os import path, remove

try:
    file_path = path.join('.', 'file_handling', 'text_files', 'my_first_file.txt')
    remove(file_path)
except FileNotFoundError:
    print('File already deleted!')
