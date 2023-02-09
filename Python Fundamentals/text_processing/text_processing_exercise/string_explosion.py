def action(symbol: str):
    if symbol == '>':
        return 'Explosion'
    if symbol.isdigit():
        return 'Change strength'


string = input()
strength = 0
result = ''

for s in string:
    todo = action(s)
    if todo == 'Explosion':
        result += '>'
    elif todo == 'Change strength':
        strength += int(s) - 1
    else:
        if strength == 0:
            result += s
        else:
            strength -= 1

print(result)