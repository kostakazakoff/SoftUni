def data_types(datatype, string: str):
    if 'int' in datatype:
        return int(string) * 2
    elif 'real' in datatype:
        return f'{float(string) * 1.5:.2f}'
    elif 'string' in datatype:
        return f'${string}$'


data_type = input()
source = input()
print(data_types(data_type, source))
