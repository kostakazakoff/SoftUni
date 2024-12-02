import time
from collections import deque

numbers = deque(map(int, input().split()))
target = int(input())

output = []

while numbers:
    first_operand = numbers.popleft()
    for _ in range(len(numbers)):
        result = first_operand + numbers[0]
        if target == result:
            output.append(f'{first_operand} + {numbers.popleft()} = {target}')
            break
        numbers.append(numbers.popleft())

[print(result) for result in output]
