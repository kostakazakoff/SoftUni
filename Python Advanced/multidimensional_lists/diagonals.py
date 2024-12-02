size = int(input())
primary_diagonal, secondary_diagonal = [], []

matrix = [(input().split(', ')) for _ in range(size)]

for i in range(size):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][-i - 1])

sum_primary_diagonal = sum([int(x) for x in primary_diagonal])
sum_secondary_diagonal = sum([int(x) for x in secondary_diagonal])

print(f'Primary diagonal: {", ".join(primary_diagonal)}. Sum: {sum_primary_diagonal}')
print(f'Secondary diagonal: {", ".join(secondary_diagonal)}. Sum: {sum_secondary_diagonal}')
