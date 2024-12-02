budget = float(input())
command = input()

while command != 'ACTION':
    name = command
    if len(name) > 15:
        sallary = 0.2 * budget
    else:
        sallary = float(input())
    budget -= sallary
    if budget <= 0:
        break
    command = input()

if budget >= 0:
    print(f'We are left with {budget:.2f} leva.')
else:
    print(f'We need {abs(budget):.2f} leva for our actors.')