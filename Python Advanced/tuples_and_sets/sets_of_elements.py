first_set_len, second_set_len = map(int, input().split())
first_set, second_set = set(), set()

[first_set.add(int(input())) for _ in range(first_set_len)]
[second_set.add(int(input())) for _ in range(second_set_len)]

[print(element) for element in first_set & second_set]