from collections import deque


queue_of_bees = deque(int(bee) for bee in input().split())
stack_of_nectar = [int(nectar) for nectar in input().split()]
operators = deque(input().split())
nectar_total = 0

while queue_of_bees and stack_of_nectar and operators:
    bee, nectar, operator = queue_of_bees.popleft(), stack_of_nectar.pop(), operators.popleft()

    if nectar < bee:
        queue_of_bees.appendleft(bee)
        operators.appendleft(operator)
        continue
    if nectar == 0:
        continue
    nectar_total += abs(eval(f'{bee}{operator}{nectar}'))

print(f'Total honey made: {nectar_total}')
if queue_of_bees:
    print(f"Bees left: {', '.join(str(bee) for bee in queue_of_bees)}")
if stack_of_nectar:
    print(f"Nectar left: {', '.join(str(nectar) for nectar in stack_of_nectar)}")