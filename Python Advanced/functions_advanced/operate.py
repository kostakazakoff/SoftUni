def operate(operator, *nums):
    return eval(f'{operator.join(str(n) for n in nums)}')


print(operate("/", 20, 4, 5))