import os


def extract_files_on_first_level(source, first_level = False):
    for file_path in os.listdir(source):
        current_path = os.path.join(source, file_path)

        if os.path.isfile(current_path):
            extension = current_path.split('.')[-1]
            if extension not in files:
                files[extension] = []
            files[extension].append(current_path)
        
        elif os.path.isdir(current_path) and not first_level:
            extract_files_on_first_level(current_path, True)


folder = input()
files = {}

extract_files_on_first_level(folder)

sorted_files = dict(sorted(files.items(), key=lambda x: x[0][0].lower()))

with open(os.path.join(folder, 'report.txt'), 'w') as file_path:
    for extension, names in sorted_files.items():
        file_path.write(f'{extension}\n')
        [file_path.write(f'- - - {name}\n') for name in sorted(names)]
