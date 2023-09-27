def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, - 1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]

    print(' '.join(str(n) for n in arr))


nums = [int(x) for x in input().split()]
insertion_sort(nums)