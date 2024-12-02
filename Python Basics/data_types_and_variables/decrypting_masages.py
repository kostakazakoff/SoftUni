key = int(input())
n = int(input())
output = ''
for i in range(n):
    crypt = input()
    decrypt = chr(ord(crypt) + key)
    output += decrypt
print(output)
