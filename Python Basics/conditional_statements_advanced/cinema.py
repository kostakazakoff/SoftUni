proj_type = input()
rows = int(input())
columns = int(input())
ticket_price = 0
if proj_type == 'Premiere':
    ticket_price = 12
elif proj_type == 'Normal':
    ticket_price = 7.5
else:
    ticket_price = 5

total_sum = rows * columns * ticket_price
print(f'{total_sum:.2f}')