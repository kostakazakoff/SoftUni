def print_triangle(num: int):
    for row in range(num * 2):
        end = row if row <= num else num * 2 - row
        print_line(end)


def print_square(num: int):
    for row in range(num):
        print_line(num)


def print_line(range_end: int):
    print(*[n for n in range(1, range_end + 1)], end=' ')
    print()