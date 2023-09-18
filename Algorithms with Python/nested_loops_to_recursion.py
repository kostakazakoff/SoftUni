def print_loops(idx, n, vector):
    if idx == n:
        print(*vector)
        return
    for i in range(n):
        vector[idx] = i + 1
        print_loops(idx+1, n, vector)


loops = int(input())
vector = [None] * loops
print_loops(0, loops, vector)