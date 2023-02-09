def bigger_or_smaller(indexed_number, removed_number):
    if indexed_number <= removed_number:
        indexed_number += removed_number
    else:
        indexed_number -= removed_number
    return indexed_number


def pokemon_catch(list_of_numbers, index):
    if index < 0:
        removed_one = list_of_numbers[0]
        list_of_numbers[0] = list_of_numbers[-1]
    elif index >= len(list_of_numbers):
        removed_one = list_of_numbers[-1]
        list_of_numbers[-1] = list_of_numbers[0]
    else:
        removed_one = list_of_numbers.pop(index)
    list_of_numbers = [bigger_or_smaller(indexed_pokemon, removed_one) for indexed_pokemon in list_of_numbers]
    return removed_one, list_of_numbers


list_of_pokemons = list(map(int, input().split()))
total = 0

while len(list_of_pokemons) > 0:
    i = int(input())
    removed, list_of_pokemons = pokemon_catch(list_of_pokemons, i)
    total += removed

print(total)
