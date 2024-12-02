clothes_stack = [int(x) for x in input().split()]
rack_capacity = int(input())
capacity = rack_capacity
racks_count = 1

while clothes_stack:
    if capacity >= clothes_stack[-1]:
        capacity -= clothes_stack.pop()
    else:
        capacity = rack_capacity
        racks_count += 1

print(racks_count)
