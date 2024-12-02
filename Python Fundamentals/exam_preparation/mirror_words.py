import re


def they_are_pairs():
    if words_pairs:
        print(f'{len(words_pairs)} word pairs found!')
        return True
    else:
        print(f'No word pairs found!')
        return False


def they_are_mirror_words():
    if len(mirrors) == 0:
        print('No mirror words!')
        return False
    return True


mirrors = []
string = input()
pattern = re.compile(r'([@#])(?P<word1>[A-Za-z]{3,})\1{2}(?P<word2>[A-Za-z]{3,})\1')

matches = re.finditer(pattern, string)
words_pairs = [[match['word1'], match['word2']] for match in matches]

if they_are_pairs():
    mirrors = [[w[0], w[1]] for w in words_pairs if w[0] == w[1][::-1]]
if they_are_mirror_words():
    output = [f'{word[0]} <=> {word[1]}' for word in mirrors]
    print('The mirror words are:')
    print(', '.join(output))
