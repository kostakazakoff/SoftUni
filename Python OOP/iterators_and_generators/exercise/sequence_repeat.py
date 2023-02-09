class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = list(sequence)
        self.count = - 1
        self.end = number

    def __iter__(self):
        return self

    def __next__(self):
        if self.count + 1 == self.end:
            raise StopIteration
        self.count += 1
        idx = self.count % len(self.sequence)
        return self.sequence[idx]

# result = sequence_repeat('I Love Python', 3)
# for item in result:
#     print(item, end ='')