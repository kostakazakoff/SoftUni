n = int(input())
l = list(str(n))
l.sort(reverse=True)


def list_to_string(l):
    s = ''
    return s.join(l)


print(list_to_string(l))