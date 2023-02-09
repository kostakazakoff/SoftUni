from collections import deque


stack_of_chocolates = [int(x) if x else 0 for x in input().split(', ')]
queue_of_milk = deque(int(x) if x else 0 for x in input().split(', '))
milkshakes = 0

while stack_of_chocolates and queue_of_milk and milkshakes < 5:
    chocolate = stack_of_chocolates.pop()
    cup_of_milk = queue_of_milk.popleft()

    if chocolate <= 0 and cup_of_milk <= 0:
        continue

    if chocolate <= 0:
        queue_of_milk.appendleft(cup_of_milk)
        continue

    if cup_of_milk <= 0:
        stack_of_chocolates.append(chocolate)
        continue

    if chocolate == cup_of_milk:
        milkshakes += 1
    else:
        stack_of_chocolates.append(chocolate - 5)
        queue_of_milk.append(cup_of_milk)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(x) for x in stack_of_chocolates) if stack_of_chocolates else 'empty'}")
print(f"Milk: {', '.join(str(x) for x in queue_of_milk) if queue_of_milk else 'empty'}")
