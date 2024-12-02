# def bubble_sort(arr):
#     nums_are_sorted = False
#     search_end = len(arr)

#     while not nums_are_sorted:
#         nums_are_sorted = True
#         for idx in range(1, search_end):
#             if arr[idx-1] > arr[idx]:
#                 arr[idx-1], arr[idx] = arr[idx], arr[idx-1]
#                 nums_are_sorted = False
#         search_end -= 1
    
#     print(' '.join(str(n) for n in arr))


def bubble_sort(arr):
    for i in range(len(arr)):
        end_of_loop = len(arr) - i
        for j in range(1, end_of_loop):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

    print(' '.join(str(n) for n in arr))


nums = [int(x) for x in input().split()]
bubble_sort(nums)