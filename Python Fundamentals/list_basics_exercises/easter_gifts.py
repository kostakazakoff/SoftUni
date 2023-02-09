gifts = input().split()
command = input()

while command != 'No Money':
    command = command.split()
    action = command[0] # first string from the list is always the action
    gift = command[1] # second string is the gift to change
    if action == 'OutOfStock':
        gifts = list(map(lambda x: 'None' if x == gift else x, gifts))
    elif action == 'Required':
        change_index = int(command[2])
        # check if the index is valid (must be smaller value than length of the list and not negative)
        if 0 <= change_index < len(gifts):
            # find the gift with the given index and change it:
            gifts[change_index] = gift
    elif action == 'JustInCase':
        gifts.pop() # removing the last in list
        gifts.append(gift) # adding the new gift at the end of list
    command = input()

gifts = [x for x in gifts if x != 'None']
gifts = ' '.join(gifts)

print(gifts)
