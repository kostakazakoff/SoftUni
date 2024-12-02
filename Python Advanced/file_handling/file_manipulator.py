from os import path, remove


def create_file(*args):
    global file_path
    file_name = args[0]
    with open(path.join(file_path, file_name), 'w') as file:
        return


def append_content(*args):
    global file_path
    file_name, content = args
    with open(path.join(file_path, file_name), 'a') as file:
        file.write(f'{content}\n')


def replace_content(*args):
    global file_path
    file_name, old_string, new_string = args
    f = path.join(file_path, file_name)
    try:
        with open(f, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print("An error occurred")
        return
    content = content.replace(old_string, new_string)
    with open(f, 'w') as file:
        file.write(content)


def delete_file(*args):
    global file_path
    file_name = args[0]
    try:
        remove(path.join(file_path, file_name))
    except FileNotFoundError:
        print("An error occurred")


file_path = path.join('.', 'file_handling', 'text_files')
command = input()

while command != 'End':
    action, *parameters = command.split('-')
    
    if action == 'Create':
        create_file(*parameters)

    elif action == 'Add':
        append_content(*parameters)

    elif action == 'Replace':
        replace_content(*parameters)

    elif action == 'Delete':
        delete_file(*parameters)

    command = input()