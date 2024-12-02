def logged(func):
    def wrapper(*args):
        resutlt = func(*args)
        return f'you called {func.__name__}{args}\nit returned {resutlt}'
    return wrapper
