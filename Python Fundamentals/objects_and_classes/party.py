class Party:
    def __init__(self):
        self.people = []


guests = []
entry = input()
party = Party()
while entry != 'End':
    party.people.append(entry)
    entry = input()

print(f'Going: {", ".join(party.people)}')
print(f'Total: {len(party.people)}')