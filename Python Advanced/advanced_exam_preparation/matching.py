from collections import deque

males = [int(x) for x in input().split()]
females = deque([int(x) for x in input().split()])
matches = 0

while males and females:
    male, female = males[-1], females[0]

    if male < 1 or female < 1:
        if male < 1: males.pop()
        if female < 1: females.popleft()
        continue
    
    elif male % 25 == 0 or female % 25 == 0:
        if male % 25 == 0: [males.pop() for _ in range(2)]
        if female % 25 == 0: [females.pop() for _ in range(2)]
        continue

    elif male != female:
        males[-1] -= 2
        females.popleft()

    else:
        matches += 1
        males.pop()
        females.popleft()

print(f"Matches: {matches}")

if males: print(f"Males left: {', '.join(str(x) for x in males[::-1])}")
else: print("Males left: none")

if females: print(f"Females left: {', '.join(str(x) for x in females)}")
else: print("Females left: none")