def decrypt(encr_message: str, instructions: list):
    operation = instructions[0]
    if operation == 'Move':
        num_of_letters = int(instructions[1])
        decr_message = f'{encr_message[num_of_letters:]}{encr_message[:num_of_letters]}'
    elif operation == 'Insert':
        i = int(instructions[1])
        v = instructions[2]
        decr_message = f'{encr_message[:i]}{v}{encr_message[i:]}'
    else:
        substr = instructions[1]
        replacement_txt = instructions[2]
        decr_message = encr_message.replace(substr, replacement_txt)
    return decr_message


message =input()

command = input()
while command != 'Decode':
    command = command.split('|')
    message = decrypt(message, command)

    command = input()

print(f'The decrypted message is: {message}')