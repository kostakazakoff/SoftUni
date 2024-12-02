def even_odd(number:int):
    if number & 1:
        print('Odd')
        return
    print('Even')


command = input()
while command != '':
    num = int(command)
    even_odd(num)
    command = input()