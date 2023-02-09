from utils.calc_helper import calc_logarithm


number = int(input())
base = input()

print(f'{calc_logarithm(number, base):.2f}')