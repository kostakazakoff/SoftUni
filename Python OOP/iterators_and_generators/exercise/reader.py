def read_next(*args):
    for el in args:
        for e in el:
            yield e


# for i in read_next("Need", (2, 3), ["words", "."]):
#     print(i)
