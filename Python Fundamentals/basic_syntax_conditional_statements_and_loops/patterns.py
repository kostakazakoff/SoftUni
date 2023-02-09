num_of_stars = int(input())

# starting a loop in the entered range:
for row in range(num_of_stars * 2):
    # printing the number of stars equal of the number of rows till row = range:
    if row <= num_of_stars:
        print(row * '*')
    # reversing the order - printing lower number of stars for the every next row till the end of the range:
    else:
        print((num_of_stars * 2 - row) * '*')
