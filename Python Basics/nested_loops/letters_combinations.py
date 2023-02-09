first = input()
second = input()
third = input()
combination = ''
combinations_counter = 0

for f in range(ord(first), ord(second) + 1):
    if chr(f) == third: continue
    for s in range(ord(first), ord(second) + 1):
        if chr(s) == third: continue
        for t in range(ord(first), ord(second) + 1):
            if chr(t) == third: continue
            combinations_counter += 1
            combination = chr(f) + chr(s) + chr(t)
            print(combination, end = ' ')
print(combinations_counter)