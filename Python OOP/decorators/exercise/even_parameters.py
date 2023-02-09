def even_parameters(func):
    def wrapper(*args):
        if all([type(x) == int for x in args]) and all([x % 2 == 0 for x in args]):
            return func(*args)         
        return "Please use only even numbers!"
    return wrapper
