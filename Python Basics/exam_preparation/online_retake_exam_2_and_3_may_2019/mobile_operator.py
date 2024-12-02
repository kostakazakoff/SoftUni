contract_term = input()
contract_type = input()
mobile_net = input()
months_payment = int(input())
tax = 0

if contract_term == 'one':
    if contract_type == 'Small':
        tax = 9.98
    elif contract_type == 'Middle':
        tax = 18.99
    elif contract_type == 'Large':
        tax = 25.98
    elif contract_type == 'ExtraLarge':
        tax = 35.99

elif contract_term == 'two':
    if contract_type == 'Small':
        tax = 8.58
    elif contract_type == 'Middle':
        tax = 17.09
    elif contract_type == 'Large':
        tax = 23.59
    elif contract_type == 'ExtraLarge':
        tax = 31.79

if mobile_net == 'yes':
    if tax <= 10:
        tax += 5.5
    elif tax <= 30:
        tax += 4.35
    else:
        tax += 3.85

if contract_term == 'two':
    tax *= 0.9625

tax *= months_payment
print(f'{tax:.2f} lv.')