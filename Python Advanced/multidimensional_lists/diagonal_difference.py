size = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(size)]

primary_diagonal = [matrix[i][i] for i in range(size)]
secondary_diagonal = [matrix[i][-1 - i] for i in range(size)]

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))
