def list_manipulator(*args):
    def add(nums, vals):
        if param == 'beginning':
            vals += nums
            nums = vals  
        else:
            nums += vals
        return nums

    def remove(nums, vals):
        if not nums: return
        if vals: n = vals[0]
        else: n = 1
        if param == "beginning":
            nums = nums[n:]
        else:
            nums = nums[:-n]
        return nums

    numbers, command1, param, *values = args
    commands = {'add': add, 'remove': remove}
    numbers = commands[command1](numbers, values)

    return numbers

# Test:
# print(list_manipulator([1,2,3], "remove", "end"))                   
# print(list_manipulator([1,2,3], "remove", "beginning"))             
# print(list_manipulator([1,2,3], "add", "beginning", 20))            
# print(list_manipulator([1,2,3], "add", "end", 30))                  
# print(list_manipulator([1,2,3], "remove", "end", 2))                
# print(list_manipulator([1,2,3], "remove", "beginning", 2))          
# print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))    
# print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))