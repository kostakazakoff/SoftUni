from collections import deque


eggs_que = deque([int(egg) for egg in input().split(', ')])
papers_stack = [int(p) for p in input().split(', ')]
box_count = 0

while eggs_que and papers_stack:
    egg = eggs_que.popleft()

    if egg <= 0: continue
    
    elif egg == 13:
        papers_stack[0], papers_stack[-1] = papers_stack[-1], papers_stack[0]
        continue

    paper = papers_stack.pop()

    if egg + paper > 50: continue

    box_count += 1

if box_count > 0: print(f'Great! You filled {box_count} boxes.')
else: print("Sorry! You couldn't fill any boxes!")

if eggs_que:
    output = [str(eggs_que.popleft()) for _ in range(len(eggs_que))]
    print(f"Eggs left: {', '.join(output)}")

if papers_stack:
    output = [str(p) for p in papers_stack]
    print(f"Pieces of paper left: {', '.join(output)}")
