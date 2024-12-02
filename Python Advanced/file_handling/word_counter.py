from os import path
import re


def create_dictionary():
    global words_to_count, words_dict
    for word in words_to_count:
        pattern = fr'\W{word}\W'
        word_count = len(re.findall(pattern, source_text, re.I))
        words_dict[word] = word_count


file_path = path.join('.', 'file_handling', 'text_files')
words = 'words.txt'
text = 'text.txt'
words_dict = {}

with open(path.join(file_path, words), 'r') as file:
    words_to_count = file.read().split()

with open(path.join(file_path, text), 'r') as file:
    source_text = file.read()

create_dictionary()

for key, value in sorted(words_dict.items(), key=lambda x: -x[1]):
    print(f'{key} - {value}')