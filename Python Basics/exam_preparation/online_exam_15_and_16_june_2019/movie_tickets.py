a1 = int(input())
a2 = int(input())
n = int(input())
ticket_number = ''
for s1 in range(a1, a2):
    s1 = chr(s1)
    for s2 in range(1, n):
        s2 = str(s2)
        n2 = int(n / 2 - 1)
        for s3 in range(1, n2+1):
            s3 = str(s3)
            s4 = str(ord(s1))
            ticket_number = s1+'-'+s2+s3+s4
            if ord(ticket_number[0]) % 2 != 0 and (int(s2) + int(s3) + int(s4)) % 2 != 0:
                print(ticket_number)