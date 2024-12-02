numbers = tuple(map(int, input().split()))
target = int(input())

used_indexes = set()
output = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if target == numbers[i] + numbers[j] and i not in used_indexes:
            output.append(f'{numbers[i]} + {numbers[j]} = {target}')
            used_indexes.update({i, j})

[print(result) for result in output]
