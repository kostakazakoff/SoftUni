def gen01(idx, n, vector):
    if idx >= len(vector):
        print(*vector, sep='')
        return
    for i in range(n):
        vector[idx] = i
        gen01(idx + 1, n, vector)

n = 2
size = int(input())
vector = [None] * size
gen01(0, n, vector)