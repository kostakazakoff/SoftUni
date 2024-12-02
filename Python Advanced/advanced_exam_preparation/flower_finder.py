from collections import deque


def flower_found():
    for name, name_chars in flowers.items():

        if vowel in name_chars:
            name_chars = name_chars.replace(vowel, '')
            flowers[name] = name_chars

        if consonant in name_chars:
            name_chars = name_chars.replace(consonant, '')
            flowers[name] = name_chars
            
        if not name_chars:
            return name


vowels = deque(input().split())
consonants = input().split()
flowers = {'rose': 'rose', 'tulip': 'tulip', 'lotus': 'lotus', 'daffodil': 'daffodil'}

while True:
    vowel = vowels.popleft()
    consonant = consonants.pop()

    found = flower_found()

    if found:
        print(f'Word found: {found}')
        break

    if not vowels or not consonants:
        break  
    
if not found: print("Cannot find any word!")
if vowels: print(f"Vowels left: {' '.join(vowels)}")
if consonants: print(f"Consonants left: {' '.join(consonants)}")