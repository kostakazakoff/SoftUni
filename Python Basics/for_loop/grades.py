students_number = int(input())
weak = 0
good = 0
very_good = 0
excelent = 0
grade_sum = 0
average = 0
for i in range(students_number):
    grade = float(input())
    if grade < 3:
        weak += 1
    elif grade < 4:
        good += 1
    elif grade < 5:
        very_good += 1
    else:
        excelent += 1
    grade_sum += grade
average = grade_sum / students_number
weak_p = weak * 100 / students_number
good_p = good * 100 / students_number
very_good_p = very_good * 100 / students_number
exceleln_p = excelent * 100 / students_number
print(f'Top students: {exceleln_p:.2f}%')
print(f'Between 4.00 and 4.99: {very_good_p:.2f}%')
print(f'Between 3.00 and 3.99: {good_p:.2f}%')
print(f'Fail: {weak_p:.2f}%')
print(f'Average: {average:.2f}')