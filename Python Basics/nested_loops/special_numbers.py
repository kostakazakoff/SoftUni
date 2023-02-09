num_to_compare = int(input())

for number in range(1111, 10000):
    number = str(number)
    number_is_special = True

    for each in number:
        if int(each) == 0 or num_to_compare % int(each) != 0:
            number_is_special = False
            continue

    if number_is_special:
        print(number, end=' ')
