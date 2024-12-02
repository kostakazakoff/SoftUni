number_of_inputs = int(input())
students_grades = {}

for _ in range(number_of_inputs):
    student, grade = input().split()
    if student not in students_grades:
        students_grades[student] = []
    students_grades[student].append(float(grade))

for name, grades in students_grades.items():
    grades_output = ' '.join([f'{grade:.2f}' for grade in grades])
    average_grade_output = f'(avg: {sum(grades) / len(grades):.2f})'
    print(f'{name} -> {grades_output} {average_grade_output}')
