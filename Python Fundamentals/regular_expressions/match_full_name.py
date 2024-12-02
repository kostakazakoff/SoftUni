import re
text = input()
names = re.findall(r'(\b[A-Z][a-z]+ [A-Z][a-z]+\b)', text)
print(' '.join(names))