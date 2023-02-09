class Stack:
    def __init__(self):
        self.values = []

    def push(self, value):
        self.values.append(value)

    def pop(self):
        return self.values.pop()

    def peek(self):
        return self.values[-1]

    def count(self):
        return len(self.values)

    def __repr__(self):
        return self.values


source_str = input()

s = Stack()
r = Stack()

for c in source_str:
    s.push(c)
while s.__repr__():
    r.push(s.pop())

print(''.join(r.__repr__()))
