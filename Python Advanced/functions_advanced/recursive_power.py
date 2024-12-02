def recursive_power(num, power):
    if power == 0:
        return 1
    return num * recursive_power(num, power - 1)


print(recursive_power(2, 10))