bottles = int(input())
floid = bottles * 750
load = 0
all_plates = 0
all_pots = 0
pots = 0
plates = 0
diff = 0
entry = ''
while floid >= 0:
    entry = input()
    if entry == 'End':
        break
    else:
        load += 1
        if load % 3 == 0:
            pots = int(entry)
            plates = 0
        else:
            plates = int(entry)
            pots = 0
        floid -= pots * 15 + plates * 5
        all_plates += plates
        all_pots += pots
        diff = abs(floid)
if floid < 0:
    print(f'Not enough detergent, {diff} ml. more necessary!')
else:
    print(f'Detergent was enough!')
    print(f'{all_plates} dishes and {all_pots} pots were washed.')
    print(f'Leftover detergent {diff} ml.')
