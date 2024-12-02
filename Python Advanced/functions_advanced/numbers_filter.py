def even_odd_filter(**kwargs):
    def even():
        return [x for x in value if x % 2 == 0]

    def odd():
        return [x for x in value if x % 2 != 0]

    for key, value in kwargs.items():
        # if key == even.__name__:
        #     kwargs[key] = even()
        # else:
        #     kwargs[key] = odd()
        kwargs[key] = eval(f'{key}()')

    return dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))