name_of_the_actor = input()
points = float(input())
judges_number = int(input())
nominee = False

for i in range(judges_number):
    judge_name = input()
    judge_points = float(input())
    points += len(judge_name) * judge_points / 2
    if points > 1250.5:
        nominee = True
        break

if nominee:
    print(f'Congratulations, {name_of_the_actor} got a nominee for leading role with {points:.1f}!')
else:
    print(f'Sorry, {name_of_the_actor} you need {(1250.5 - points):.1f} more!')
