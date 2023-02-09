def even_odd(*args):
    def even():
        return [x for x in args[:-1] if x % 2 == 0]

    def odd():
        return [x for x in args[:-1] if x % 2 != 0]

    return eval(f'{args[-1]}()')


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))