def selection_sort(arr):
    for i in range (len(arr)):
        curr_num = arr[i]
        min_num = curr_num

        for next_i in range(i+1, len(arr)):
            if arr[next_i] < min_num:
                min_num = arr[next_i]
                arr[next_i], arr[i] = arr[i], arr[next_i]

    return ' '.join(str(n) for n in arr)


nums = [int(x) for x in input().split()]
print(selection_sort(nums))