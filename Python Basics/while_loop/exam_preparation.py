number_of_bad_grades = int(input())
exam_name = input()
grade = int(input())
number_of_problems = 0
bad_grades_counter = 0
sum_of_grades = 0
average_score = 0
enough = False
fail = False
while not fail:
    last_problem_name = exam_name
    number_of_problems += 1
    sum_of_grades += grade
    if grade <= 4:
        bad_grades_counter += 1
    if bad_grades_counter == number_of_bad_grades:
        fail = True
        break
    exam_name = input()
    if exam_name == 'Enough':
        enough = True
        break
    grade = int(input())


average_score = sum_of_grades / number_of_problems
if fail:
    print(f'You need a break, {bad_grades_counter} poor grades.')
if enough:
    print(f'Average score: {average_score:.2f}')
    print(f'Number of problems: {number_of_problems}')
    print(f'Last problem: {last_problem_name}')