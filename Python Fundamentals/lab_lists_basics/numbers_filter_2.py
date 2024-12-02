integers_count = int(input())
integers = [int(input()) for _ in range(integers_count)]
command = input()
result = []


def filter_int(definition, list_of_integers):
    for i in list_of_integers:
        filter_integers = (
            (definition == 'even' and i % 2 == 0),
            (definition == 'odd' and i % 2 != 0),
            (definition == 'positive' and i >= 0),
            (definition == 'negative' and i < 0)
        )
        if any(filter_integers):
            result.append(i)
    return result


print(filter_int(command, integers))
