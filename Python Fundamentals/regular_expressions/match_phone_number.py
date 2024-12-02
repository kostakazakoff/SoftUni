from re import findall

text = input()
valid_phones = findall(r'\+359 2 [0-9]{3} [0-9]{4}\b|\+359-2-[0-9]{3}-[0-9]{4}\b', text)
print(', '.join(valid_phones))