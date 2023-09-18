class ChessPad:
    def __init__(self, matrix):
        self.matrix = matrix
        self.used_rows = set()
        self.used_cols = set()
        self.used_left_diags = set()
        self.used_right_diags = set()


matrix = [['-'] * 8 for _ in range(8)]
gamepad = ChessPad(matrix)


def put_queens(row):
    if row == 8:
        [print(*x) for x in gamepad.matrix]
        print()
        return
    for col in range(8):
        if is_posible(row, col):
            set_queen(row, col)
            put_queens(row+1)
            remove_queen(row, col)


def is_posible(row, col):
    if row < 0 or col < 0 or col >= 8:
        return False
    if gamepad.matrix[row][col] == '*':
        return False
    if row in gamepad.used_rows\
        or col in gamepad.used_cols\
        or row - col in gamepad.used_left_diags\
        or row + col in gamepad.used_right_diags:
            return False
    return True
    

def set_queen(row, col):
    gamepad.matrix[row][col] = '*'
    gamepad.used_rows.add(row)
    gamepad.used_cols.add(col)
    gamepad.used_left_diags.add(row-col)
    gamepad.used_right_diags.add(row+col)


def remove_queen(row, col):
    gamepad.matrix[row][col] = '-'
    gamepad.used_rows.remove(row)
    gamepad.used_cols.remove(col)
    gamepad.used_left_diags.remove(row-col)
    gamepad.used_right_diags.remove(row+col)


put_queens(0)