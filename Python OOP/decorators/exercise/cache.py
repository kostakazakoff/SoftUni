def cache(func):
    def wrapper(n):    
        if n in wrapper.log:
            return wrapper.log[n]
        wrapper.log[n] = func(n)
        return wrapper.log[n]   
    wrapper.log = {}
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# print(fibonacci(50))
# print(fibonacci.log) 