def words_sorting(*args):
    words_dict = {}
    for word in args:
        word_value = sum([ord(x) for x in word])
        words_dict.update({word: word_value})
        odd = sum(words_dict.values()) % 2
    words_dict = dict(sorted(words_dict.items(), key=lambda x: -x[1] if odd else x[0]))
    return '\n'.join([f'{k} - {v}' for k, v in words_dict.items()])


print(
    words_sorting(
        'escape', 
        'charm', 
        'mythology'
  ))