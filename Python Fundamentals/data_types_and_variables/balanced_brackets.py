n = int(input())
balanced = True
open_bracket = False
closed_bracket = True

for i in range(n):
    simbol = input()

    if simbol == '(':
        if not closed_bracket:
            balanced = False
            break
        else:
            closed_bracket = False

    elif simbol == ')':
        if closed_bracket:
            balanced = False
            break
        else:
            closed_bracket = True

if balanced:
    print('BALANCED')
else:
    print('UNBALANCED')