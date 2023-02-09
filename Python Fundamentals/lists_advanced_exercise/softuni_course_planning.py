def input_treatment(course_list: str):
    if len(course_list) == 0:
        values = []
    else:
        values = course_list.split(', ')
    pack = {'Lesson': None}
    course_list = []
    lessons = [x for x in values if len(x.split('-')) == 1]
    exercises = [x for x in values if len(x.split('-')) == 2]
    for lesson in lessons:
        pack = pack.copy()
        pack['Lesson'] = lesson
        course_list.append(pack)
    for exercise in exercises:
        for i in range(len(course_list)):
            course_list[i]['Exercise'] = exercise if course_list[i]['Lesson'] in exercise else 'None'
    return course_list


def content_not_in_list(course_list: list, lesson: str):
    for i in range(len(course_list)):
        if lesson == course_list[i]['Lesson']:
            return False
    return True


def add_content(course_list: list, lesson:str):
    if not content_not_in_list(course_list, lesson):
        return course_list
    course_list.append({'Lesson': lesson})
    return course_list


def insert_content(course_list: list, lesson: str, index: int):
    if not content_not_in_list(course_list, lesson):
        return course_list
    course_list.insert(index, {'Lesson': lesson})
    return course_list


def remove_content(course_list: list, lesson: str):
    if content_not_in_list(course_list, lesson):
        return course_list
    for i in range(len(course_list)):
        if lesson == course_list[i]['Lesson']:
            course_list.pop(i)
            return course_list


def swap_contents(course_list: list, lesson_1: str, lesson_2: str):
    if content_not_in_list(course_list, lesson_1) or content_not_in_list(course_list, lesson_2):
        return course_list
    for ind in range(len(course_list)):
        if lesson_1 == course_list[ind]['Lesson']:
            i_1 = ind
        if lesson_2 == course_list[ind]['Lesson']:
            i_2 = ind
    course_list[i_1], course_list[i_2] = course_list[i_2], course_list[i_1]
    return course_list


def import_exercise(course_list: list, new_exercise: str):
    lesson = new_exercise.split('-')[0]
    if content_not_in_list(course_list, lesson):
        for i in range(len(course_list)):
            if lesson == course_list[i]['Lesson']:
                course_list[i]['Exercise'] = new_exercise
                return course_list
    course_list.append({'Lesson': lesson, 'Exercise': new_exercise})
    return course_list


course = input()
course = input_treatment(course)
command = input()

while command != 'course start':
    command = command.split(':')
    action = command[0]
    lesson_title = command[1]
    if action == 'Add':
        course = add_content(course, lesson_title)
    elif action == 'Insert':
        i = int(command[2])
        course = insert_content(course, lesson_title, i)
    elif action == 'Remove':
        course = remove_content(course, lesson_title)
    elif action == 'Swap':
        lesson_title_2 = command[2]
        course = swap_contents(course, lesson_title, lesson_title_2)
    elif action == 'Exercise':
        lesson_title = f'{lesson_title}-Exercise'
        course = import_exercise(course, lesson_title)
    command = input()

count = 1
output = ''
for package in course:
    for v in package.values():
        output += f'{count}.{v}\n'
        count += 1
print(output)