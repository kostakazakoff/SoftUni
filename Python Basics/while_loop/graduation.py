student_name = input()
years = 0
sum_grade = 0
fail_count = 0
while years < 12:
    if fail_count > 1:
        break
    grade = float(input())
    if grade < 4:
        fail_count += 1
        continue
    sum_grade += grade
    years += 1
if fail_count > 1:
    print(f'{student_name} has been excluded at {years+1} grade')
else:
    average = sum_grade / years
    print(f'{student_name} graduated. Average grade: {average:.2f}')