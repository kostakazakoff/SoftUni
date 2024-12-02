def tribonacci(count):
    tribonacci_numbers = [1]
    for _ in range(count - 1):
        number = sum(tribonacci_numbers[:-4:-1])
        tribonacci_numbers.append(number)
    return tribonacci_numbers


count_of_tribonacci_numbers = int(input())
result = tribonacci(count_of_tribonacci_numbers)
print(*result)
