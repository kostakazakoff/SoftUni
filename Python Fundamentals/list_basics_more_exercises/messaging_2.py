numbers = input().split()
source = input()


def message_encode(strings_of_numbers, source_message):
    # creating a list of simbols, needed for the task:
    source_message = [x for x in source_message]
    message = ''
    
    # iterating to extract the codes from the numbers list:
    for code in strings_of_numbers:
        # taking the sum of code integers
        # it's the searched index of the symbol in the source message list:
        i = sum(int(x) for x in code)
        # if the end of the source message list is exceeded,
        # start from the first index (using a division by remainder):
        if i > len(source_message):
            i %= len(source_message)
        # appending the message string, removing the value in the source message:
        message += source_message.pop(i)
    return message


print(message_encode(numbers, source))
