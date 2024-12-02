def solution():
    def integers():
        number = 0        
        while True:
            number += 1
            yield number

    def halves():
        for n in integers():
            yield n / 2

    def take(n, seq):
        return [next(seq) for _ in range(n)]

    return take, halves, integers


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
