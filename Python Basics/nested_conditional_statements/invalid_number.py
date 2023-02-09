# Var. 1
# number = int(input())
# if number < 100 or number > 200:
#     if number != 0:
#         print('invalid')

# Var. 2
number = int(input())
valid = (number < 100 or number > 200) and number != 0
if not valid:
    print('invalid')