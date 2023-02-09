width = int(input())
lenght = int(input())
cake = width * lenght
no_more_cake = False
diff = 0
command = input()
while command != 'STOP':
    pieces_of_cake = int(command)
    cake -= pieces_of_cake
    if cake < 0:
        no_more_cake = True
        break
    command = input()
if no_more_cake:
    print(f"No more cake left! You need {abs(cake)} pieces more.")
if command == 'STOP' and cake > 0:
    print(f'{cake} pieces are left.')