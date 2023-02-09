def search_for_queen(direct, r, c):
    global chessboard, danger
    while chessboard[r][c] != 'Q':
        r, c = r + direct[0], c + direct[1]
        if not all((0 <= r < 8, 0 <= c < 8)):
            return
        if chessboard[r][c] == 'Q':
            print(f'[{r}, {c}]')
            danger = True


chessboard = []
directions = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, 1), (1, -1))
danger = False

for row in range(8):
    rank = input().split()
    if 'K' in rank: king_r, king_c = row, rank.index('K')
    chessboard.append(rank)

for direction in directions: search_for_queen(direction, king_r, king_c)

if not danger: print("The king is safe!")