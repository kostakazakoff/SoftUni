from os import listdir, path


files_dict = {}
source_path = input()
all_paths = [source_path]

# Extract and append the first level directories to all_paths list for traversing-----------------
for file_path in listdir(source_path):
    path_to_check = path.join(source_path, file_path)
    if path.isdir(path_to_check):
        all_paths.append(path_to_check)

# Traversing the directories from the all_paths list----------------------------------------------
for sub_path in all_paths:
    for file_path in listdir(sub_path):
        if path.isdir(path.join(sub_path, file_path)):
            continue # escaping the directories
    
        file_extension = file_path.split('.')[-1]

        # adding file extensions and files into the dictionary------------------------------------
        if file_extension not in files_dict:
            files_dict[file_extension] = []
        files_dict[file_extension].append(file_path)

# Sorting and saving the result to report.txt file------------------------------------------------
sorted_files = dict(sorted(files_dict.items(), key=lambda x: x[0][0].lower()))

with open(path.join(source_path, 'report.txt'), 'w') as file_path:
    for extension, names in sorted_files.items():
        file_path.write(f'{extension}\n')
        [file_path.write(f'- - - {name}\n') for name in sorted(names)]