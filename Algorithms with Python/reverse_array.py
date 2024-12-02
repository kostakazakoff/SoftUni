def reverse_arr(arr, idx = 0):
    if idx >= len(arr)// 2:
        print(*arr, sep=' ')
        return
    arr[idx], arr[len(arr) - idx - 1] = arr[len(arr) - idx - 1], arr[idx]
    reverse_arr(arr, idx + 1)


array = input().split(' ')
reverse_arr(array)


# def reverse_arr(arr, count, reversed_arr):
#     if count == len(arr):
#         print(*reversed_arr, sep=' ')
#         return
#     reversed_arr.append(arr[-count - 1])
#     reverse_arr(arr, count + 1, reversed_arr)


# array = input().split(' ')
# reverse_arr(array, 0, [])
