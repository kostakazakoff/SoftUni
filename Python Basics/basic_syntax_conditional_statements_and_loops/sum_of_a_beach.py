expression = input()
expression = expression.lower()
result = 0
options = ['sand', 'water', 'fish', 'sun']
for o in options:
    result += expression.count(o)
print(result)
