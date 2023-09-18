# def move(row, col, rows, cols):
#     global count
#     if row >= rows or col >= cols:
#         return
#     if row == rows - 1 or col == cols - 1:
#         count += 1
#         return
    
#     move(row, col+1, rows, cols)
#     move(row+1, col, rows, cols)

# rows = int(input())
# cols = int(input())
# count = 0
# move(0, 0, rows, cols)
# print(count)


def move(row, col, rows, cols):
    if row >= rows or col >= cols:
        return 0
    if row == rows - 1 or col == cols - 1:
        return 1
    
    count = 0
    
    count += move(row, col+1, rows, cols)
    count += move(row+1, col, rows, cols)

    return count


rows = int(input())
cols = int(input())
print(move(0, 0, rows, cols))
