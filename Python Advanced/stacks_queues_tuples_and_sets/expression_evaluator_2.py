import math
from collections import deque


def operation():
    global numbers, operators, expression, result
    operator = element
    operation_sequence = []
    while numbers:
        operation_sequence.append(numbers.popleft())
    operation_sequence = operator.join(operation_sequence)
    result = math.floor(eval(operation_sequence))
    numbers.appendleft(str(result))


numbers = deque()
operators = ('*', '/', '+', '-')
result = 0
expression = (x for x in input().split())

for element in expression:
    if element not in operators:
        numbers.append(element)
    else:
        while len(numbers) > 1:
            operation()

print(result)
