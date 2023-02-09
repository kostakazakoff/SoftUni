first = input()
list_first = [int(x) for x in str(first)]
last = input()
list_last = [int(x) for x in str(last)]
barcodes = ''

for n in range(int(first), int(last) + 1):
    chk_list = []
    check_list = [int(x) for x in str(n)]
    for i in range(len(check_list)):
        if check_list[i] % 2 != 0 and list_first[i] <= check_list[i] <= list_last[i]:
            chk_list.append(n)
    if len(chk_list) == len(check_list):
        barcodes += str(n) + ' '

print(barcodes)