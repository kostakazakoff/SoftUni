num = int(input())


def prime_num_checker(n):
    is_prime = True
    for i in range(2, n):
        if n % i == 0 and n != 2:
            is_prime = False
    return is_prime


print(prime_num_checker(num))
