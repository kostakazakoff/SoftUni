import re

string = input()
destinations = []
pattern = re.compile(r'([=/])(?P<destination>[A-Z][A-Za-z]{2,})\1')

matches = re.finditer(pattern, string)
for match in matches:
    if match:
        destinations.append(match['destination'])

travel_points = sum(len(x) for x in destinations)
destinations = ', '.join(destinations)
print(f'Destinations: {destinations}')
print(f'Travel Points: {travel_points}')
