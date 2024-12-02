key = [int(x) for x in input().split()]
string = input()

while string != 'find':
    result = ''
    for i in range(len(string)):
        result += chr(ord(string[i]) - key[i % len(key)])

    result = result.split('&')
    coordinates = result[-1].split('<')[-1][:-1]
    print(f'Found {result[1]} at {coordinates}')
    string = input()