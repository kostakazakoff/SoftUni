def reverse_arr(arr, idx = 0):
    if idx >= len(arr)// 2:
        print(*arr, sep=' ')
        return
    arr[idx], arr[len(arr) - idx - 1] = arr[len(arr) - idx - 1], arr[idx]
    reverse_arr(arr, idx + 1)

array = input().split(' ')
reverse_arr(array)
