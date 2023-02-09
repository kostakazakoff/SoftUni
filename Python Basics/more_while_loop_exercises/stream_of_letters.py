command = []
secret = ''
entry = ''
while entry != 'End':
    entry = input()
    if not entry.isalpha():
        continue
    if (entry == 'c' or entry == 'o' or entry == 'n') and entry not in command:
        command.append(entry)
        entry = ''
    if 'c' in command and 'o' in command and 'n' in command:
        print(secret, end=' ')
        secret = ''
        command = []
    else:
        secret += entry
