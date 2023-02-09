number_of_strings = int(input())
word = input()
the_list_of_strings = [input() for x in range(number_of_strings)]


def word_exist_in_the_list(the_word, the_list):
    output = []
    for string in the_list:
        if the_word in string:
            output.append(string)
    return output


print(the_list_of_strings)
print(word_exist_in_the_list(word, the_list_of_strings))