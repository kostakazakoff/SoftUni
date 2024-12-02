string_1 = input()
string_2 = input()

while string_1 in string_2:
    string_2 = string_2.replace(string_1, '')

print(string_2)