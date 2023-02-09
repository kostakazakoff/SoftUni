from math import ceil

persons = int(input())
elevator_capacity = int(input())
courses = 0 if elevator_capacity <= 0 else ceil(persons / elevator_capacity)

print(courses)