number_of_messages = int(input())

for _ in range(number_of_messages):
    number = int(input())
    if number == 88:
        message = 'Hello'
    elif number == 86:
        message = 'How are you?'
    elif number < 88:
        message = 'GREAT!'
    else:
        message = 'Bye.'
    print(message)
