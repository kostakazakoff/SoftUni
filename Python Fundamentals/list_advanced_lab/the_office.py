def happiness(employees: str, factor: int):
    employees = list(map(int, employees.split()))
    employees_happiness = [employee * factor for employee in employees]
    average_happiness = sum(employees_happiness) / len(employees_happiness)
    happy_count = len([x for x in employees_happiness if x >= average_happiness])
    are_happy = happy_count >= len(employees_happiness) / 2
    return happy_count, are_happy


input_employees = input()
factor_of_happiness = int(input())

number_of_happy_employees, employees_are_happy = happiness(input_employees, factor_of_happiness)

if employees_are_happy:
    print(f"Score: {number_of_happy_employees}/{len(input_employees.split())}. Employees are happy!")
else:
    print(f"Score: {number_of_happy_employees}/{len(input_employees.split())}. Employees are not happy!")