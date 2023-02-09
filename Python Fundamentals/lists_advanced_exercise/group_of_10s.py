def groups_of_10(numbers: str):
    numbers = list(map(int, numbers.split(', ')))
    group_range_start, group_range_end, group_of_10, group_name, result = 0, 10, [], [], []
    while len(numbers) > 0:
        # add a list of numbers group range (range step 10) to the result list:
        group_of_10.append(list(filter(lambda x: group_range_start < x <= group_range_end, numbers)))
        # filtering the source list (removing the numbers with values in the range, added to the result):
        numbers = list(filter(lambda x: x > group_range_end, numbers))
        # add a values of the range group name to the group_name list:
        group_name.append(group_range_end)
        # lift the start, end values of the range group (0 to 10, 10 to 20... etc.)
        group_range_start += 10
        group_range_end += 10
    for index, name in enumerate(group_name):
        result.append(f'Group of {name}\'s: {group_of_10[index]}')
    return '\n'.join(result)


nums = input()
print(groups_of_10(nums))
