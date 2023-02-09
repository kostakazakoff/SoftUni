import re

total = 0
string = input()

while string != 'end of shift':
    match = re.search(r'%(?P<name>[A-Z]{1}[a-z]+)%.*<(?P<product>\w+)>.*\|(?P<count>\d+)\|\D*(?P<price>\d+\.?\d+)\$', string)
    if match:
        visitor_summary = int(match['count']) * float(match['price'])
        print(f'{match["name"]}: {match["product"]} - {visitor_summary:.2f}')
        total += visitor_summary
    string = input()

print(f'Total income: {total:.2f}')
