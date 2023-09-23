def get_target_index(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        midle = (left + right) // 2

        if numbers[midle] == target:
            return midle
        
        elif target < numbers[midle]:
            right = midle - 1
        
        else:
            left = midle + 1
    
    return -1


arr = [int(n) for n in input().split()]
target_num = int(input())

print(get_target_index(arr, target_num))