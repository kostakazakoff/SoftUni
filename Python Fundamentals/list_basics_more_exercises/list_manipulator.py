numbers = input()
numbers = list(map(int, numbers.split()))
command = input()


def even_odd(definition, integers):
    output = []
    if definition == 'even':
        # creating a list of even integers:
        output = list(x for x in integers if x % 2 == 0)
    # creating a list of odd integers:
    elif definition == 'odd':
        output = list(x for x in integers if x % 2 != 0)
    return output


while command != 'end':
    copy = []
    command = command.split() # converting the command string to list
    action = command[0] # first index content is alwais an action command
    
    if action == 'exchange':
        index = int(command[1])
         # checking the index validity
        if index < 0 or index >= len(numbers):
            print('Invalid index')
        else:
            # changing the places of the two parts of the list (separated by the given index),
            # using the slicing function:
            numbers = numbers[(index + 1):] + numbers[:index + 1]
    
    # for these two actions we have a similar operations:
    elif action == 'max' or action == 'min':
        num_type = command[1] # the type of the number is alwais in the second index
        # creating a list of even/odd numbers, depending the function (num_type) input:
        copy = even_odd(num_type, numbers)
        # if there is not a result for the number type in the list:
        if len(copy) == 0:
            print('No matches')
        else:
            # taking the minimum and maximum values from the prepared "copy" list:
            searched_number = min(copy) if action == 'min' else max(copy)
            # inverting the source list, ensure finding the last number with the searched value:
            numbers.reverse()
            # it's the first one in this case:
            searched_index = numbers.index(searched_number) + 1
            print(len(numbers) - searched_index)
            # invert back the source list to the original condition:
            numbers.reverse()
    
    # for these two actions we have a similar operations again:
    elif action == 'first' or action == 'last':
        result = [] # preparing a list for the results
        count = int(command[1]) # the count of the values is alwais in the second index of command
        num_type = command[2] # the type of the number is alwais in the third index of command
        # checking the count validity:
        if len(numbers) >= count > 0:
            # creating a list of even/odd numbers, depending the function (num_type) input:
            copy = even_odd(num_type, numbers)
            if action == 'first':
                # filling up the result list with the counted values as posible
                # no more than the numbers count in the copy list:
                result = [copy[x] for x in range(count) if len(copy) > x]
            elif action == 'last':
                # making the same operations, but from the reversed list of results
                # because we need the last numbers in this case:
                copy.reverse()
                result = [copy[x] for x in range(count) if len(copy) > x]
                # invert the result list to the right condition (because the reverted source is used):
                result.reverse()
            print(result)
        else:
            print('Invalid count')
    command = input()

print(numbers)
