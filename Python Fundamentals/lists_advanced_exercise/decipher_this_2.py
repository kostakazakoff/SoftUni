# Problem solved using the strings manipulation
def decipher_message(ciphered_string: str):
    # separating the message:
    list_to_decipher = ciphered_string.split()
    deciphered = ''
    # processing the parts(words):
    for content in list_to_decipher:
        # extracting the numbers from the word:
        ascii_value = ''.join([ch for ch in content if ch.isdigit()])
        # extracting the characters from the word:
        characters = ''.join([ch for ch in content if ch.isalpha()])
        # replacing the first and the last character (if they are):
        if len(characters) >= 2:
            characters = f'{characters[-1]}{characters[1:-1]}{characters[0]}'
        # adding the result word to the deciphered string:
        deciphered += f'{chr(int(ascii_value))}{characters} '
    return deciphered


ciphered_message = input()
print(decipher_message(ciphered_message))
