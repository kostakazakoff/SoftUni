def students_per_h(support_1: int, support_2: int, support_3: int):
    return support_1 + support_2 + support_3


def time_to_complete(students_per_hour: int, count_of_students: int):
    hours = count_of_students // students_per_hour
    students_left = count_of_students % students_per_hour > 0
    if students_left:
        hours += 1
    if hours < 4:
        return hours
    hours_to_rest = hours // 3
    if hours_to_rest:
        hours += hours_to_rest
    return hours


support_1_capacity = int(input())
support_2_capacity = int(input())
support_3_capacity = int(input())
number_of_students = int(input())

students_per_h_result = students_per_h(support_1_capacity, support_2_capacity, support_3_capacity)
time = time_to_complete(students_per_h_result, number_of_students)
print(f'Time needed: {time}h.')

# Тази задаче вероятно е предложена от някой служител към support отдела :))))