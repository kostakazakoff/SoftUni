def perfect_number(number: int):
    result = sum(n for n in range(1, number) if number % n == 0)
    if result == number:
        return 'We have a perfect number!'
    return "It's not so perfect."


num = int(input())
print(perfect_number(num))
