def odd_even_sum(source: str):
    numbers = list(int(x) for x in source)
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    odds = list(filter(lambda x: x % 2 != 0, numbers))

    def odd_sum():
        return sum(odds)

    def even_sum():
        return sum(evens)

    print(f'Odd sum = {odd_sum()}, Even sum = {even_sum()}')


source_number = input()
odd_even_sum(source_number)
