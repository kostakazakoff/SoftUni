from utils.calc_helper import calc_expression


result = calc_expression(input())
if type(result) == float:
    print(f'{result:.2f}')