def banned_replacing(string: str, words: list):
    for word in words:
        string = string.replace(word, '*' * len(word))
    return string


banned_words = input().split(', ')
text = banned_replacing(input(), banned_words)
print(text)