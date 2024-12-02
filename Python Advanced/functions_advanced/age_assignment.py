def age_assignment(*args, **kwargs):
    def get_name_by_first_letter():
        for name in args:
            if name.startswith(letter):
                return name

    result = {}

    for letter, age in kwargs.items():
        result.update({get_name_by_first_letter(): age})

    output = dict(sorted(result.items())).items()

    return '\n'.join([f'{name} is {age} years old.' for name, age in output])


print(age_assignment("Peter", "George", G=26, P=19))