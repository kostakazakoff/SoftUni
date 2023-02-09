def vowel_filter(function):
    def wrapper():
        return [x for x in function() if x.lower() in {'a','e','i','o','u'}]
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]
print(get_letters())