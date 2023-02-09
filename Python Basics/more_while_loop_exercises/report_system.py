needed_sum = int(input())
end = False
collected_sum = 0
payment = ''
count = 0
cash_payment = 0
card_payment = 0
cash_transaction = 0
card_transaction = 0
while collected_sum < needed_sum:
    payment = input()
    if payment != 'End':
        payment = int(payment)
    else:
        end = True
        break
    count += 1
    if count % 2 != 0 and payment <= 100:
        cash_payment += int(payment)
        cash_transaction += 1
        print('Product sold!')
    elif count % 2 == 0 and payment >= 10:
        card_payment += int(payment)
        card_transaction += 1
        print('Product sold!')
    else:
        print('Error in transaction!')
        continue
    collected_sum = card_payment + cash_payment
    if cash_transaction > 0:
        average_cs = cash_payment / cash_transaction
    else:
        average_cs = 0
    if card_transaction > 0:
        average_cc = card_payment / card_transaction
    else:
        average_cc = 0
if end:
    print('Failed to collect required money for charity.')
else:
    print(f'Average CS: {average_cs:.2f}')
    print(f'Average CC: {average_cc:.2f}')
