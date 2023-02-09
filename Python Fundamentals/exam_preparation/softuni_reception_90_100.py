def time_to_complete(students_per_hour: int, students_count: int):
    hours = students_count // students_per_hour
    students_left = students_count % students_per_hour > 0
    if students_left:
        hours += 1
    if hours < 4:
        return hours
    hours_to_rest = hours // 3
    if hours_to_rest:
        hours += hours_to_rest
    return hours


s1, s2, s3 = int(input()), int(input()), int(input())
students_per_h = s1 + s2 + s3
number_of_students = int(input())

time = time_to_complete(students_per_h, number_of_students)
print(f'Time needed: {time}h.')
