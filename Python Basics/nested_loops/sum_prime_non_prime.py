prime_numbers_sum = 0
nonprime_numbers_sum = 0
number_is_negative = False
command = input()

while command != 'stop':
    number = int(command)
    if number < 0:
        print('Number is negative.')
        command = input()
        continue
    number_is_nonprime = False
    for i in range (2, number):
        if number % i == 0:
            number_is_nonprime = True
    if number_is_nonprime:
        nonprime_numbers_sum += number
    else:
        prime_numbers_sum += number
    command = input()

print(f'Sum of all prime numbers is: {prime_numbers_sum}')
print(f'Sum of all non prime numbers is: {nonprime_numbers_sum}')