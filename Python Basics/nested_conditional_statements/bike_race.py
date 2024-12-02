junior_bikers = int(input())
senior_bikers = int(input())
trace_type = input()
junior_personal_tax = 0
senior_personal_tax = 0
tax_summary = 0
discount = 0
all_bikers = junior_bikers + senior_bikers
if trace_type == 'trail':
    junior_personal_tax = 5.5
    senior_personal_tax = 7
elif trace_type == 'cross-country':
    junior_personal_tax = 8
    senior_personal_tax = 9.5
    if all_bikers >= 50:
        discount = 0.25
elif trace_type == 'downhill':
    junior_personal_tax = 12.25
    senior_personal_tax = 13.75
elif trace_type == 'road':
    junior_personal_tax = 20
    senior_personal_tax = 21.5
tax_summary = junior_personal_tax * junior_bikers + senior_personal_tax * senior_bikers
tax_summary = tax_summary - tax_summary * discount
tax_summary -= tax_summary * 0.05
print(f'{tax_summary:.2f}')
