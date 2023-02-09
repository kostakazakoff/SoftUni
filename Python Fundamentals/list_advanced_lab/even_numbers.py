def even_numbers_position(string_of_numbers: str):
    numbers = list(map(int, string_of_numbers.split(', ')))
    return [num for num in range(len(numbers)) if numbers[num] % 2 == 0]


n_string = input()
print(even_numbers_position(n_string))