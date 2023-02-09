def sorting_names(input_string: str):
    list_of_names = input_string.split(', ')
    list_of_names.sort(key= lambda name: (-len(name), name))
    return list_of_names


names = input()
print(sorting_names(names))