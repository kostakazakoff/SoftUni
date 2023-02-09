from collections import deque


def empty_cups():
    global stack_of_chocolate, queue_of_milk
    if stack_of_chocolate[-1] > 0 and queue_of_milk[0] > 0:
        return False
    if stack_of_chocolate[-1] <= 0:
        stack_of_chocolate.pop()
    if queue_of_milk[0] <= 0:
        queue_of_milk.popleft()
    return True


def make_a_shake():
    global stack_of_chocolate, queue_of_milk, milkshakes
    cup_of_milk = queue_of_milk.popleft()
    chocolate = stack_of_chocolate.pop()
    ready_to_shake = chocolate == cup_of_milk
    if ready_to_shake:
        milkshakes += 1
        return
    queue_of_milk.append(cup_of_milk)
    stack_of_chocolate.append(chocolate - 5)


stack_of_chocolate = [int(x) if x else 0 for x in input().split(', ')]
queue_of_milk = deque(int(x) if x else 0 for x in input().split(', '))
milkshakes = 0

while stack_of_chocolate and queue_of_milk and milkshakes < 5:
    if empty_cups():
        continue
    make_a_shake()

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(x) for x in stack_of_chocolate) if stack_of_chocolate else 'empty'}")

print(f"Milk: {', '.join(str(x) for x in queue_of_milk) if queue_of_milk else 'empty'}")
