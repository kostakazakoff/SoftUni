class Fibonacci:
    def __init__(self):
        self.casche = {}

    def sequence(self, n):
        if n <= 1:
            return 1
        if n not in self.casche:
            self.casche[n] = self.sequence(n-1) + self.sequence(n-2)
        return self.casche[n]


n = int(input())
fibonacci = Fibonacci()
print(fibonacci.sequence(n))