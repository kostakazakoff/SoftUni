string_1 = input().split(', ')
string_2 = input().split(', ')

substring = list(filter(lambda x: x in str(string_2), string_1))
print(substring)
