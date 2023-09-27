def bubble_sort(arr):
    nums_are_sorted = False
    search_end = len(arr)
    while not nums_are_sorted:
        nums_are_sorted = True
        for idx in range(1, search_end):
            if arr[idx-1] > arr[idx]:
                arr[idx-1], arr[idx] = arr[idx], arr[idx-1]
                nums_are_sorted = False
        search_end -= 1
    
    return ' '.join(str(n) for n in arr)


nums = [int(x) for x in input().split()]
print(bubble_sort(nums))