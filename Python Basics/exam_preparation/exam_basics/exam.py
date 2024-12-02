students = int(input())
total_evaluation = 0
top_students = 0
to_5_students = 0
to_4_students = 0
fail_students = 0

for any_student in range(students):
    judge = float(input())
    if judge >= 5:
        top_students += 1
    elif judge >= 4:
        to_5_students += 1
    elif judge >= 3:
        to_4_students += 1
    else:
        fail_students += 1
    total_evaluation += judge

percent_top = top_students / students * 100
percent_to_5 = to_5_students / students * 100
percent_to_4 = to_4_students / students * 100
percent_to_3 = fail_students / students * 100
average_evaluation = total_evaluation / students

print(f'Top students: {percent_top:.2f}%')
print(f'Between 4.00 and 4.99: {percent_to_5:.2f}%')
print(f'Between 3.00 and 3.99: {percent_to_4:.2f}%')
print(f'Fail: {percent_to_3:.2f}%')
print(f'Average: {average_evaluation:.2f}')