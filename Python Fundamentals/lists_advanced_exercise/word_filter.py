text = list(input().split())
even_length_words = list(filter(lambda x: len(x) % 2 == 0, text))
# for word in even_length_words:
#     print(word)
print('\n'.join(even_length_words))
