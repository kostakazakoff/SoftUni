command = input()
calc = 0
vowels = 'AaEeIiOoUuYy'
max_number = 0
most_powerfull_word = ''
while command != 'End of words':
    word = command
    for i in range(len(word)):
        calc += ord(word[i])
    if word[0] in vowels:
        calc *= len(word)
    else:
        calc //= len(word)
    if calc > max_number:
        max_number = calc
        most_powerfull_word = word
    calc = 0
    command = input()

print(f'The most powerful word is {most_powerfull_word} - {max_number}')