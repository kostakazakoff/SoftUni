from collections import deque


def best_list_pureness(*args):
    numbers, count = args
    numbers = deque([int(x) for x in numbers])
    numbers_length = len(numbers)
    best_pureness = sum([numbers[i] * i for i in range(numbers_length)])
    rotations = 0

    for rotation in range(1, count + 1):
        numbers.rotate()
        pureness = sum([numbers[i] * i for i in range(numbers_length)])

        if pureness > best_pureness:
            best_pureness = pureness
            rotations = rotation

    return f'Best pureness {best_pureness} after {rotations} rotations'


# Test:
# test = ([4, 3, 2, 6], 4)
# result = best_list_pureness(*test)
# print(result)