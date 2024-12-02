def characters_in_range(start_index, end_index):
    char_stream = list(chr(x) for x in range(ord(start_index) + 1, ord(end_index)))
    return ' '.join(char_stream)


char_start = input()
char_end = input()

print(characters_in_range(char_start, char_end))
