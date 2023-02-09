actor_name = input()
points = float(input())
number_of_judges = int(input())
judge_name = ''
judge_points = 0
is_nominee = False
for i in range(number_of_judges):
    judge_name = input()
    judge_points = float(input())
    points += len(judge_name) * judge_points / 2
    if points > 1250.5:
        is_nominee = True
        break
diff = 1250.5 - points
if is_nominee:
    print(f'Congratulations, {actor_name} got a nominee for leading role with {points:.1f}!')
else:
    print(f'Sorry, {actor_name} you need {diff:.1f} more!')

