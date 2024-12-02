# Input the neighborhood (house numbers):
neighborhearts = list(map(int, input().split('@')))
command = input()
house = 0

while command != 'Love!':
    command = command.split()
    # increase the number of the last house visited:
    house += int(command[1])

    # ensure that the house with that number is in the neighborhood (if not in range, jump to the first one):
    if house >= len(neighborhearts):
        house = 0

    # Enter a bool variable, witch shows the house has Valentine's Day:
    valentine = neighborhearts[house] == True

    # Fill up the house with love (2 hearts) if there is not a Valentine's Day in there:
    if not valentine:
        neighborhearts[house] -= 2
        # If the house is full of love, print it and enter Valentine's Day in this address:
        if neighborhearts[house] <= 0:
            print(f'Place {house} has Valentine\'s day.')
            neighborhearts[house] = True
    # The house is already in love :)
    else:
        print(f'Place {house} already had Valentine\'s day.')

    command = input()

print(f'Cupid\'s last position was {house}.')

# Create a list of completed (True) and uncompleted (False) house missions:
neighborhearts = list(map(lambda x: x if x == True else False, neighborhearts))

# If all houses have Valentine's Day (check if all bools are True) and print the good news:
if all(neighborhearts):
    print('Mission was successful.')
# Cupid's mission not accomplished:
else:
    # Create a list with a failed house missions and print the result:
    failed = len(list(filter(lambda x: x == False, neighborhearts)))
    print(f'Cupid has failed {failed} places.')
