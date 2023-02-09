def extract(string: str):
    person = ''
    age = ''
    extract_person = False
    extract_age = False
    operators = {'@': {'Person': True}, '|': {'Person': False}, '#': {'Age': True}, '*': {'Age': False}}
    for s in string:
        if s in operators:
            param = {k: v for k, v in operators.items() if k == s}
            if 'Person' in operators[s]:
                extract_person = param[s]['Person']
                continue
            elif 'Age' in operators[s]:
                extract_age = param[s]['Age']
                continue

        if extract_person:
            person += s
        elif extract_age:
            age += s
    return person, age


persons = int(input())
for _ in range(persons):
    person, age = extract(input())
    print(f'{person} is {age} years old.')
