entry = input()
total_sum = 0
while entry != 'NoMoreMoney':
    entry = float(entry)
    if entry < 0:
        print('Invalid operation!')
        break
    total_sum += entry
    print(f'Increase: {entry:.2f}')
    entry = input()

print(f'Total: {total_sum:.2f}')