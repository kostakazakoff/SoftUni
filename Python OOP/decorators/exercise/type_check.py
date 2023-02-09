def type_check(arg_type):
    def decorator(func_ref):
        def wrapper(*args):
            for argument in args:
                if type(argument) is not arg_type:
                    return "Bad Type"
            result = func_ref(*args)
            return result     
        return wrapper
    return decorator


# @type_check(str) 
# def first_letter(word): 
#     return word[0] 

# print(first_letter('Hello World')) 
# print(first_letter(['Not', 'A', 'String'])) 