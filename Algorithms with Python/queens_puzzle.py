class ChessPad:
    def __init__(self, matrix):
        self.matrix = matrix
        self.used_rows = set()
        self.used_cols = set()
        self.used_left_diags = set()
        self.used_right_diags = set()

    def set_queen(self, row, col):
        self.matrix[row][col] = '*'
        self.used_rows.add(row)
        self.used_cols.add(col)
        self.used_left_diags.add(row-col)
        self.used_right_diags.add(row+col)

    def remove_queen(self, row, col):
        self.matrix[row][col] = '-'
        self.used_rows.remove(row)
        self.used_cols.remove(col)
        self.used_left_diags.remove(row-col)
        self.used_right_diags.remove(row+col)

    def position_is_free(self, row, col):
        if col < 0 or col >= len(self.matrix[0]):
            return False
        if self.matrix[row][col] == '*':
            return False
        if row in self.used_rows\
            or col in self.used_cols\
            or row - col in self.used_left_diags\
            or row + col in self.used_right_diags:
                return False
        return True


def put_queens(row):
    if row == 8:
        [print(*x) for x in gamepad.matrix]
        print()
        return
    for col in range(8):
        if gamepad.position_is_free(row, col):
            gamepad.set_queen(row, col)
            put_queens(row+1)
            gamepad.remove_queen(row, col)


size = 8
matrix = [['-'] * size for _ in range(size)]
gamepad = ChessPad(matrix)


put_queens(0)