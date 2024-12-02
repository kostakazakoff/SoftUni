n = int(input())


def prime_number_checker(n):
    prime = True
    for i in range(2, n):
        if n != 2 and n % i == 0:
            prime = False
            break
    return prime


print(prime_number_checker(n))