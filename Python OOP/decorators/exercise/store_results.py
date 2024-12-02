def store_results(func):
    def wrapper(*args):
        print(f"Function '{func.__name__}' was add called. Result: {func(*args)}")
    return wrapper


@store_results 
def add(a, b): 
    return a + b 


@store_results 
def mult(a, b): 
    return a * b 


add(2, 2) 
mult(6, 4) 
