string = input()
output = []
for i, s in enumerate(string):
    if s.isupper():
        output.append(i)
print(output)