first_num = int(input())
last_num = int(input())
magic_num = int(input())
all_combinations = 0
combinations = False
for n1 in range(first_num, last_num + 1):
    for n2 in range(first_num, last_num + 1):
        all_combinations += 1
        if magic_num > last_num * 2: # saving resources
            continue
        if n1 + n2 == magic_num:
            combinations = True
            print(f'Combination N:{all_combinations} ({n1} + {n2} = {magic_num})')
    if combinations:
        break
if not combinations:
    print(f'{all_combinations} combinations - neither equals {magic_num}')