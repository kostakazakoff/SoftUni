number_of_invited = int(input())
invited = set()
arrived = set()

for _ in range(number_of_invited):
    invited.add(input())

arrival = input()
while arrival != 'END':
    arrived.add(arrival)
    arrival = input()

missing_guests = invited - arrived

vip_list = set([guest for guest in sorted(missing_guests) if guest[0].isdigit()])
regulars_list = missing_guests - vip_list

print(len(missing_guests))
[print(guest) for guest in sorted(vip_list)]
[print(guest) for guest in sorted(regulars_list)]
