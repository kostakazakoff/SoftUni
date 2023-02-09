mylist = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x > 3, mylist[2::2]))
print(result)