expression = input()
operation = ''
left_bracket_index = []

for i in range(len(expression)):
    if expression[i] == '(':
        left_bracket_index.append(i)
    elif expression[i] == ')':
        right_bracket_index = i + 1
        print(expression[left_bracket_index.pop():right_bracket_index])
