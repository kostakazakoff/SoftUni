def even_integers(numbers_as_str: list):
    list_of_integers = list(map(int, numbers_as_str))

    def even_filter(integer: int):
        return integer % 2 == 0

    return list(filter(even_filter, list_of_integers))


numbers = input().split()
print(even_integers(numbers))
