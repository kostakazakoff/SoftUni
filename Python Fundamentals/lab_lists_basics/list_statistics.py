count_of_numbers = int(input())
numbers = [int(input()) for _ in range(count_of_numbers)]
positive = [x for x in numbers if x >= 0]
negative = [x for x in numbers if x < 0]
print(positive)
print(negative)
print(f'Count of positives: {len(positive)}')
print(f'Sum of negatives: {sum(negative)}')
