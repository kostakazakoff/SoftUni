from itertools import permutations


def possible_permutations(x):
    p = permutations(x)
    for any in p:
        yield list(any)


# [print(n) for n in possible_permutations([1, 2, 3])]