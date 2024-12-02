open_tabs = int(input())
salary = float(input())
tax = 0
salary_is_finished = False
for i in range(open_tabs):
    site = input()
    if site == 'Facebook':
        tax += 150
    elif site == 'Instagram':
        tax += 100
    elif site == 'Reddit':
        tax += 50
    if tax >= salary:
        salary_is_finished = True
diff = salary - tax
if salary_is_finished:
    print('You have lost your salary.')
else:
    print(int(diff))
