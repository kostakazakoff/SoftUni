def sum_array(idx, nums):
    if idx == len(nums) - 1:
        return nums[idx]
    return nums[idx] + sum_array(idx + 1, nums)

arr = [int(x) for x in input().split(' ')]
print(sum_array(0, arr))