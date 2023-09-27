nums = [int(x) for x in input().split()]

for i in range (len(nums)):
    curr_num = nums[i]
    min_num = curr_num

    for next_i in range(i+1, len(nums)):
        if nums[next_i] < min_num:
            min_num = nums[next_i]
            nums[next_i], nums[i] = nums[i], nums[next_i]

print(*nums, sep=' ')