from collections import defaultdict


def add_exam(results_dict: defaultdict, submissions_dict: defaultdict, student, prog_language, exam_points):
    results_dict[student].append(exam_points)
    submissions_dict[prog_language].append(exam_points)
    return results_dict, submissions_dict


def bann_user(results_dict: defaultdict, student):
    results_dict.pop(student)
    return results_dict


def print_exam_results(results_dict: defaultdict):
    print('Results:')
    [print(f'{name} | {max(points)}') for name, points in results_dict.items()]


def print_submissions(submissions_dict: defaultdict):
    print('Submissions:')
    [print(f'{prog_language} - {len(exam_submissions)}') for prog_language, exam_submissions in submissions_dict.items()]


exam_results = defaultdict(list)
submissions = defaultdict(list)

command = input().split('-')
while command[0] != 'exam finished':
    username = command[0]
    if command[1] == 'banned':
        exam_results = bann_user(exam_results, username)
        command = input().split('-')
        continue
    language, points = command[1], int(command[2])
    exam_results, submissions = add_exam(exam_results, submissions, username, language, points)

    command = input().split('-')

print_exam_results(exam_results)
print_submissions(submissions)
