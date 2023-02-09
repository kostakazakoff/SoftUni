def balanced(left_p, right_p):
    match = ('()', '[]', '{}')
    extracted_parentheses = f'{left_p}{right_p}'
    if extracted_parentheses in match:
        return True
    return False


parentheses = list(input())
left_parentheses = ('(', '[', '{')
right_parentheses = (')', ']', '}')
left_stack = []
balanced_parentheses = True

if len(parentheses) % 2 != 0:
    print('NO')
    exit()

for p in parentheses:
    if p in left_parentheses:
        left_stack.append(p)
    elif p in right_parentheses:
        if not left_stack or not balanced(left_stack.pop(), p):
            print('NO')
            balanced_parentheses = False
            break

if balanced_parentheses:
    print('YES')
