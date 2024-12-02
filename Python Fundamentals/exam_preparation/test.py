import re

# cleaners = {}
#
#
# def add_cleaner(func):
#     cleaners[func.__name__] = func
#     return func
#
#
# @add_cleaner
# def email():
#    return 'O.K.'
#
#
# print(cleaners)


# def multiply(*numbers):
#     x = 1
#     for n in numbers:
#         x *= n
#     return x
#
#
# list_of_numbers = range(1, 10)
#
# print(multiply(*list_of_numbers))


# string = 'In the Sofia Zoo there are 311 animals in total! ::Smiley:: This includes 3 **Tigers**, 1 ::Elephant:, 12 **Monk3ys**, a **Gorilla::, 5 ::fox:es: and 21 different types of :Snak::Es::. ::Mooning:: **Shy**'
# emojis = re.finditer(r'([:*]{2})[A-Z][a-z]{2,}\1', string)
# for x in emojis:
#     print(x.group())
