class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.number = start - 1 if end > start else start + 1
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.number == self.end:
            raise StopIteration
        self.number = self.number + 1 if self.end > self.start else self.number - 1
        return self.number


# one_to_ten = custom_range(1, 10)
# for num in one_to_ten:
#     print(num)