number_of_lines = int(input())
unique_elements = set()

for _ in range(number_of_lines):
    [unique_elements.add(element) for element in input().split()]

[print(element) for element in unique_elements]