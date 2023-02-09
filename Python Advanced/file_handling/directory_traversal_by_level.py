import os


def extract_files_by_level(source, level_to_extract):
    for file_path in os.listdir(source):
        current_path = os.path.join(source, file_path)

        if os.path.isfile(current_path):
            extension = current_path.split('.')[-1]
            if extension not in files:
                files[extension] = []
            files[extension].append(file_path)
        
        elif os.path.isdir(current_path) and level_to_extract:
            extract_files_by_level(current_path, level_to_extract - 1)


folder = input('Enter the directory to traverse: ')
level = int(input('Enter the traversing level: '))
files = {}

extract_files_by_level(folder, level)

sorted_files = dict(sorted(files.items(), key=lambda x: x[0][0].lower()))

with open(os.path.join(folder, 'report.txt'), 'w') as file_path:
    for extension, names in sorted_files.items():
        file_path.write(f'{extension}\n')
        [file_path.write(f'- - - {name}\n') for name in sorted(names)]
