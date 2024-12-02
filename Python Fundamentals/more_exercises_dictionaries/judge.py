def add_result(judge: dict, student: str, exam: str, result: int):
    if exam not in judge:
        judge[exam] = {}
    if student not in judge[exam] or result >= judge[exam][student]:
        judge[exam][student] = result
    return judge


def print_statistic(judge: dict):
    individual = {}
    for exam, values in judge.items():
        print(f'{exam}: {len(values)} participants')
        count = 0
        exam_ordered = dict(sorted(judge[exam].items(), key=lambda item: (-item[1], item[0])))
        for student, result in exam_ordered.items():
            count += 1
            print(f'{count}. {student} <::> {result}')
            if student not in individual:
                individual[student] = 0
            individual[student] += result
    individual = dict(sorted(individual.items(), key=lambda item: (-item[1], item[0])))
    print('Individual standings:')
    count = 0
    for student, result in individual.items():
        count += 1
        print(f'{count}. {student} -> {result}')


students = {}
command = input().split(' -> ')
while command[0] != 'no more time':
    name, contest, points = command[0], command[1], int(command[2])
    students = add_result(students, name, contest, points)

    command = input().split(' -> ')

print_statistic(students)
