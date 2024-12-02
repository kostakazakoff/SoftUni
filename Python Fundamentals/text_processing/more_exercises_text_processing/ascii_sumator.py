startsimbol, endsimbol = ord(input()), ord(input())
string = input()
result = sum([ord(x) for x in string if startsimbol < ord(x) < endsimbol])
print(result)
