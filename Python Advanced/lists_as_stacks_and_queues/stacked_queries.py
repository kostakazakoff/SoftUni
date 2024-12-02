class Stack:
    def __init__(self):
        self.values = []

    def operation_1(self, value):
        return self.values.append(value)

    def operation_2(self):
        if self.values:
            return self.values.pop()

    def operation_3(self):
        if self.values:
            print(max(self.values))

    def operation_4(self):
        if self.values:
            print(min(self.values))

    def reverse_stack(self):
        if not self.values:
            return
        s_copy = self.values.copy()
        self.values.clear()
        while s_copy:
            self.values.append(s_copy.pop())

    def __repr__(self):
        return self.values


s = Stack()
number_of_lines = int(input())

for _ in range(number_of_lines):
    command = list(map(int, input().split()))
    action = command[0]
    if action == 1:
        s.operation_1(command[1])
    elif action == 2:
        s.operation_2()
    elif action == 3:
        s.operation_3()
    elif action == 4:
        s.operation_4()

s.reverse_stack()
output = list(map(str, s.__repr__()))
output = ', '.join(output)
print(output)