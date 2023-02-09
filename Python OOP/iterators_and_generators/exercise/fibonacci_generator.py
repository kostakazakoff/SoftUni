# 1 --------------------------------------------------

# def fibonacci():
#     first = -1
#     second = 1
#     while True:
#         third = first + second
#         yield third
#         first, second = second, third

# 2 -------------------------------------------------

def fibonacci():
    first = 0
    second = 1
    while True:
        yield first
        first, second = second, first + second

# Test -----------------------------------------------

# generator = fibonacci()
# for i in range(10):
#     print(next(generator))