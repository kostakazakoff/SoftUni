content = input().split()
step = int(input())

index = 0
result = []
finished = False

# iterating while the content list is not empty:
while not finished:
    index += step - 1
    # if out of index, start from the begining:
    if index >= len(content):
        index %= len(content)
    # transfer the value with current index from the content list to the result list
    # and removing the value from the content list:
    result.append(content.pop(index))
    # defining the "finished" value (if the content list is empty = True)
    finished = len(content) == 0

# preparing the result as in the task conditions:
separator = ','
print(f'[{separator.join(result)}]')
