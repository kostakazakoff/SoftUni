def func_executor(*args):
    result = []
    for command in args:
        func = command[0]
        values = command[1]
        result.append(f'{func.__name__} - {func(*values)}')
    return '\n'.join(result)


def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result


def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result


print(func_executor(
    (make_upper, ("Python", "softUni")),
    (make_lower, ("PyThOn",)),
))
