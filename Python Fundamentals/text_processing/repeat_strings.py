words = input().split()
[print(''.join(word * len(word)), end = '') for word in words]
