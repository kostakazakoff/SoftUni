a = int(input())
b = int(input())
max_passwords = int(input())
aa = 35
bb = 64
combinations = 0
for x in range(1, a + 1):
    for y in range(1, b + 1):
        print(f'{chr(aa)}{chr(bb)}{x}{y}{chr(bb)}{chr(aa)}', end='|')
        aa += 1
        bb += 1
        combinations += 1
        if aa > 55: aa = 35
        if bb > 96: bb = 64
        if combinations == max_passwords: exit()