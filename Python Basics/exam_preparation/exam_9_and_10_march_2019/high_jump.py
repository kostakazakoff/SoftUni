needed_heigh = int(input())
loaded_heigh = needed_heigh - 35
jump_heigh = 0
jump_counter = 0
try_counter = 0
training_is_fail = False
while loaded_heigh < needed_heigh:
    loaded_heigh += 5
    jump_heigh = 0
    try_counter = 0
    while jump_heigh <= loaded_heigh and try_counter < 3:
        jump_heigh = int(input())
        jump_counter += 1
        try_counter += 1

    if jump_heigh <= loaded_heigh and try_counter == 3:
        training_is_fail = True
        break

if training_is_fail:
    print(f'Tihomir failed at {loaded_heigh}cm after {jump_counter} jumps.')
else:
    print(f'Tihomir succeeded, he jumped over {loaded_heigh}cm after {jump_counter} jumps.')
