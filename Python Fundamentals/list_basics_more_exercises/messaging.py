strings_of_numbers = input().split()
source = input()
source = [x for x in source]
message = ''
for code in strings_of_numbers:
    i = sum(int(x) for x in code)
    if i > len(source):
        i %= len(source)
    message += source.pop(i)
print(message)
