def max_contiguous_subarray(numbers: list):
    # if len(numbers) == 1:
    #     return  numbers[0]
    # results = {}
    # for i in range(1, len(numbers)):
    #     for j in range(i, 0, -1):
    #         sub_arr = numbers[i-j:i] + numbers[i:i+j]
    #         results[sum(sub_arr)] = sub_arr
    # result = sorted(results.items(), reverse=True)
    # return result[0][1]

    cur_sum = 0
    start = 0
    temp_start = 0
    end = 0
    max_sum = 0

    for i in range(len(numbers)):
        if numbers[i] > numbers[i] + cur_sum:
            cur_sum = numbers[i]
            temp_start = i
        else:
            cur_sum += numbers[i]
        if cur_sum > max_sum:
            max_sum = cur_sum
            start = temp_start
            end = i

    return numbers[start:end+1]


nums = [int(x) for x in input().split()]
print(max_contiguous_subarray(nums))

# 1 2 -5 2 4 -3 2 -3
