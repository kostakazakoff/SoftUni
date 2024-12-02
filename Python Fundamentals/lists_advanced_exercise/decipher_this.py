# Problem solved using the list manipulation
def decipher_message(ciphered_string: str):
    list_to_decipher = ciphered_string.split()
    ascii_values = []
    characters = []

    for content in list_to_decipher:
        # create a list with the extracted ASCII numbers (strings) from the strings in the source list:
        ascii_values.append(''.join(list(filter(lambda x: str(x).isdigit(), content))))
        # creating a list with the extracted alphabetic characters from the source list:
        characters.append(list(filter(lambda x: str(x).isalpha(), content)))

    # converting ASCII (strings) numbers to integers:
    ascii_characters = list(map(lambda x: chr(int(x)), ascii_values))

    # prepare an empty list for the deciphered result:
    deciphered = []

    # rotate the first and last character places:
    for i in range(len(characters)):
        if len(characters[i]) >= 2:
            # change the character places (first and last one):
            characters[i][0], characters[i][-1] = characters[i][-1], characters[i][0]
        # append to decipher a list of strings from the deciphered lists:
        deciphered.append(ascii_characters[i] + ''.join(characters[i]))
    # create a string from list:
    deciphered = ' '.join(deciphered)
    return deciphered


ciphered_message = input()
print(decipher_message(ciphered_message))
