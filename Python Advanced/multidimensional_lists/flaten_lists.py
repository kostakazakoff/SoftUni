input_list = input().split('|')
result_list = []
output = []

[result_list.append([int(x) for x in sublist.split()]) for sublist in input_list[::-1]]
[output.extend(sublist) for sublist in result_list]
print(*output)
