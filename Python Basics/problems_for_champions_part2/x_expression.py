expression = input()
operator = '+'
in_operation = False
result = 0
in_result = 0

for simbol in expression:

        if simbol == '=':
            break

        if simbol == '+' or simbol == '-' or simbol == '*' or simbol == '/':
            if in_operation:
                in_operator = simbol
            else:
                operator = simbol
            continue

        elif simbol == '(':
            in_operation = True
            in_operator = '+'
            number = 0

        elif simbol == ')':
            in_operation = False
            number = in_result
            in_result = 0

        elif 48 <= ord(simbol) <= 57:
            number = int(simbol)

        if in_operation:
            if in_operator == '+':
                in_result += number
            elif in_operator == '-':
                in_result -= number
            elif in_operator == '*':
                in_result *= number
            elif in_operator == '/':
                in_result /= number
        else:
            if operator == '+':
                result += number
            elif operator == '-':
                result -= number
            elif operator == '*':
                result *= number
            elif operator == '/':
                result /= number

print(f'{result:.2f}')

