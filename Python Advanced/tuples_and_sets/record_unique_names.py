number_of_lines = int(input())
unique = set()
for _ in range(number_of_lines):
    unique.add(input())
[print(name) for name in unique]
