class dictionary_iter:
    def __init__(self, dictionary: dict) -> None:
        self.dict_items = list(dictionary.items())
        self.idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx + 1 == len(self.dict_items):
            raise StopIteration
        self.idx += 1
        return self.dict_items[self.idx]


# result = dictionary_iter({"name": "Peter", "age": 24})
# for x in result:
#     print(x)