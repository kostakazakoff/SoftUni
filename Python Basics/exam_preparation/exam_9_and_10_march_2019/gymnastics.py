team = input()
discipline = input()
points = 0
if team == 'Russia':
    if discipline =='ribbon':
        points = 9.1 + 9.4
    elif discipline == 'hoop':
        points = 9.3 + 9.8
    elif discipline == 'rope':
        points = 9.6 + 9
elif team == 'Bulgaria':
    if discipline == 'ribbon':
        points = 9.6 + 9.4
    elif discipline == 'hoop':
        points = 9.55 + 9.75
    elif discipline == 'rope':
        points = 9.5 + 9.4
elif team == 'Italy':
    if discipline == 'ribbon':
        points = 9.2 + 9.5
    elif discipline == 'hoop':
        points = 9.45 + 9.35
    elif discipline == 'rope':
        points = 9.7 + 9.15
diff = (20 - points) * 100 / 20
print(f'The team of {team} get {points:.3f} on {discipline}.')
print(f'{diff:.2f}%')