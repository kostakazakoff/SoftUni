entry = ''
tired = False
steps = 0
all_steps = 0
diff = 0
steps_to_home = 0
while all_steps <= 10000:
    command = input()
    if command == 'Going home':
        tired = True
        steps_to_home = int(input())
        break
    steps = int(command)
    all_steps += steps
diff = 10000 - all_steps - steps_to_home
if tired and diff > 0:
    print(f'{diff} more steps to reach goal.')
else:
    print('Goal reached! Good job!')
    print(f'{abs(diff)} steps over the goal!')