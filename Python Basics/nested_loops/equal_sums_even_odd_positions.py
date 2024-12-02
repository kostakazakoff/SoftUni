start = int(input())
end = int(input())

for number in range(start, end + 1):
    odd_num = 0
    even_num = 0
    string_number = str(number)
    for index, num in enumerate(string_number):
        if index % 2 == 0:
            odd_num += int(num)
        else:
            even_num += int(num)
    if odd_num == even_num:
        print(number, end = ' ')