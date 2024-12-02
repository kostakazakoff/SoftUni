class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        element = self.data[-1]
        del self.data[-1]
        return element

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        output = ', '.join(x for x in reversed(self.data))
        return f'[{output}]'
