def palindrome_integer(list_of_integers):
    for integer in list_of_integers:
        integer = list(integer)
        palindrome = integer[:] == integer[::-1]
        print(palindrome)


numbers = list(input().split(', '))
palindrome_integer(numbers)
