class vowels:
    def __init__(self, string):
        self.string = list(string)
        self.idx = -1
        self.vowels = [x for x in self.string if x.lower() in {'a','e','i','o','u'}]

    def __iter__(self):
        return self

    def __next__(self):
        self.idx += 1
        if self.idx == len(self.vowels):
            raise StopIteration
        char = self.vowels[self.idx]
        return char


# my_string = vowels('Abcedifuty0o')
# for char in my_string:
#     print(char)