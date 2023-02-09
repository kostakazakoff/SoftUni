from collections import deque


def operation():
    global numbers, operators, expression, result
    operator = element
    first_num = numbers.popleft()
    second_num = numbers.popleft()
    if operator == '+':
        result = first_num + second_num
    elif operator == '-':
        result = first_num - second_num
    elif operator == '*':
        result = first_num * second_num
    elif operator == '/':
        result = first_num // second_num
    numbers.appendleft(result)


numbers = deque()
operators = ('*', '/', '+', '-')
result = 0
expression = (int(x) if x not in operators else x for x in input().split())

for element in expression:
    if element not in operators:
        numbers.append(element)
    else:
        while len(numbers) > 1:
            operation()

print(result)
