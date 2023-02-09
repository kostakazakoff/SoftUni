import re


def decrypt():
    global message
    key = len(re.findall(r'[star]', message, re.I))
    message = ''.join([chr(ord(s) - key) for s in message])


def message_info():
    global message, planets
    match = re.search(r'@(?P<planet>[A-Za-z]+).*:(?P<population>\d+).*(?P<type>[AD])!.*->(?P<soldiers>\d+)', message)
    if match:
        if match.group('type') == 'A':
            attacked_planets.append(match.group('planet'))
        else:
            destroyed_planets.append(match.group('planet'))


messages_count = int(input())
planets = {}
attacked_planets = []
destroyed_planets = []

for _ in range(messages_count):
    message = input()
    decrypt()
    message_info()

print(f'Attacked planets: {len(attacked_planets)}')
if attacked_planets:
    [print(f'-> {name}') for name in sorted(attacked_planets)]
print(f'Destroyed planets: {len(destroyed_planets)}')
if destroyed_planets:
    [print(f'-> {name}') for name in sorted(destroyed_planets)]
