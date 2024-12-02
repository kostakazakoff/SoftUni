def get_primes(nums: list):
    for n in nums:
        if n < 2:
            continue
        for number in range(2, n):
            if n % number == 0:
                break
        else:
            yield n


# print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))