class reverse_iter:
    def __init__(self, iterable_obj):
        self.iterable_obj = iterable_obj
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx == -len(self.iterable_obj):
            raise StopIteration
        self.idx -= 1
        return self.iterable_obj[self.idx]


# reversed_list = reverse_iter([1, 2, 3, 4])
# for item in reversed_list:
#     print(item)