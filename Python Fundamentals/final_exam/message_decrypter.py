import re

messages_count = int(input())

for _ in range(messages_count):
    message = input()
    pattern = r'^([$%])(?P<tag>[A-Z][a-z]{2,})\1: \[(\d+)\]\|\[(\d+)\]\|\[(\d+)\]\|$'
    match = re.search(pattern, message)
    if not match:
        print('Valid message not found!')
        continue
    n1, n2, n3 = [int(x) for x in match.groups()[2:]]
    tag = match.groups()[1]
    print(f'{tag}: {chr(n1)}{chr(n2)}{chr(n3)}')
