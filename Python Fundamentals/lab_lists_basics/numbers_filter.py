integers_count = int(input())
integers = [int(input()) for _ in range(integers_count)]
command = input()
EVEN = 'even'
ODD = 'odd'
NEGATIVE = 'negative'
POSITIVE = 'positive'
result = []
for i in integers:
    filter_integers = (
        command == EVEN and i % 2 == 0 or
        command == ODD and i % 2 != 0 or
        command == NEGATIVE and i < 0 or
        command == POSITIVE and i >= 0
    )
    if filter_integers:
        result.append(i)
print(result)