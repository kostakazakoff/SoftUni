source = input()
counter = int(input())

repeat = lambda string, count: string * count

result = repeat(source, counter)
print(result)
