n = int(input())
positives = []
negatives = []

for i in range(n):
    value = int(input())
    positives.append(value) if value >= 0 else negatives.append(value)

print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}")
print(f'Sum of negatives: {sum(negatives)}')
