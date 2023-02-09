first = list(input())
second = list(input())

for i in range(len(first)):
    if first[i] != second[i]:
        first[i] = second[i]
        print(''.join(first))
