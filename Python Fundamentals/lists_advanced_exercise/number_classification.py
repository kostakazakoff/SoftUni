def numbers_classification(numbers: str):
    numbers = list(map(int, numbers.split(', ')))
    positive = ', '.join([str(x) for x in numbers if x >= 0])
    negative = ', '.join([str(x) for x in numbers if x < 0])
    even = ', '.join([str(x) for x in numbers if x % 2 == 0])
    odd = ', '.join([str(x) for x in numbers if x % 2 != 0])
    print(f'Positive: {positive}')
    print(f'Negative: {negative}')
    print(f'Even: {even}')
    print(f'Odd: {odd}')


nums = input()
numbers_classification(nums)