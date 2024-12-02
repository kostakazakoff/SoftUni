def start_spring(**kwargs):
    objects_dict = {}
    output = ''

    for k, v in kwargs.items():
        if v not in objects_dict:
            objects_dict[v] = []
        objects_dict[v].append(k)

    for k, v in dict(sorted(objects_dict.items(), key=lambda x: (-len(x[1]), x[0]))).items():
        output += f'{k}:\n'
        if v:
            v = "\n-".join(sorted(v))
            output += f'-{v}\n'
            
    return output


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))