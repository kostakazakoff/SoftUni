def sorting_cheeses(**kwargs):
    sorted_cheese = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    output = ''
    for k, v in sorted_cheese:
        v = sorted(v, reverse=True)
        output += f'{k}\n'
        output += "\n".join([str(x) for x in v]) + '\n'
    return output


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
