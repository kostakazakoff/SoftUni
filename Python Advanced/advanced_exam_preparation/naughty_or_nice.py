def naughty_or_nice_list(*args, **kwargs):
    santa_dict = {"Nice": [], "Naughty": [], "Not found": []}
    santa_list = [x for x in args if type(x) == list][0]
    arguments = [[int(y) if y.isdigit() else y for y in x.split('-')] for x in args if type(x) == str]

    santa_source_dict = {}
    for l in santa_list:
        if l[0] not in santa_source_dict:
            santa_source_dict.update({l[0]: []})
        santa_source_dict[l[0]].append(l[1])

    for a in arguments:
        if a[0] in santa_source_dict and len(santa_source_dict[a[0]]) == 1:
            santa_dict[a[1]].append(santa_source_dict[a[0]][0])
            del santa_source_dict[a[0]]

    santa_source_dict_2 = {}
    for name, values in santa_source_dict.items():
        for n in values:
            if n not in santa_source_dict_2:
                santa_source_dict_2.update({n: []})
            santa_source_dict_2[n].append(name)

    for name, v in kwargs.items():
        if name in santa_source_dict_2 and len(santa_source_dict_2[name]) == 1:
            santa_dict[v].append(name)
            del santa_source_dict_2[name]

    for name, values in santa_source_dict_2.items():
        if not values:
            continue
        for _ in range(len(values)):
            santa_dict["Not found"].append(name)

    output = ''

    for k, names in santa_dict.items():
        if names:
            names = ', '.join(names)
            output += f'{k}: {names}\n'

    return output
            
    


print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))