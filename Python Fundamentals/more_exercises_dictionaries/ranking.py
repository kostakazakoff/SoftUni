def add_result(results: dict, student: str, exam: str, points: int):
    if student not in results:
        results[student] = {}
    if exam not in results[student]:
        results[student][exam] = 0
    if points > results[student][exam]:
        results[student][exam] = points
    return results


def print_best_candidate(results: dict):
    rank_list = {}
    for candidate, contests in results.items():
        total_points = sum([x for x in contests.values()])
        rank_list[candidate] = total_points
    highest_result = 0
    best = ''
    for name, contest_points in rank_list.items():
        if contest_points > highest_result:
            highest_result = contest_points
            best = name
    print(f'Best candidate is {best} with total {highest_result} contest_points.')


def print_ranking(results: dict):
    results = dict(sorted(results.items(), key=lambda item: item[0]))
    print('Ranking:')
    for candidate in results:
        print(candidate)
        candidate_results = dict(sorted(results[candidate].items(),reverse=True, key=lambda item: item[1]))
        for contest, result in candidate_results.items():
            print(f'#  {contest} -> {result}')


contests = {}
contest_results = {}
command = input().split(':')
while command[0] != 'end of contests':
    exam, password = command[0], command[1]
    contests[exam] = password
    command = input().split(':')

command = input().split('=>')
while command[0] != 'end of submissions':
    exam, password, student, points = command[0], command[1], command[2], int(command[3])
    if exam in contests.keys() and password in contests.values():
        contest_results = add_result(contest_results, student, exam, points)
    command = input().split('=>')

print_best_candidate(contest_results)
print_ranking(contest_results)