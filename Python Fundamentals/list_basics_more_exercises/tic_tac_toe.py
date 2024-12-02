# creating a lists of the line/row values from the input:
l1 = list(map(int, filter(lambda x: x != ' ', input())))
l2 = list(map(int, filter(lambda x: x != ' ', input())))
l3 = list(map(int, filter(lambda x: x != ' ', input())))


def tic_tac_toe(row_1, row_2, row_3):
    # creating a 2 dimensional gamepad matrix table:
    gamepad = [row_1, row_2, row_3]
    result = ''
    
    # two iterations (straight and reversed gamepad)
    # because to check the diagonal values from the top-left to the bottom-right position
    # for the example:
    # 1 0 0 and 0 0 1
    # 0 1 0     0 1 0
    # 0 0 1     1 0 0 second table must be inverted to use the same operation:
    for _ in range(2):
        # reset the diagonal results for the second use:
        diagonal = []
        for i in range(3):
            # the row values
            row = gamepad[i]
            # the column values:
            column = [row_1[i], row_2[i], row_3[i]]
            # the diagonal values
            diagonal += [gamepad[i][i]]
            if row.count(1) == 3 or column.count(1) == 3 or diagonal.count(1) == 3:
                result = 'First player won'
                break # keeping the system resources (if there is a winner, no more actions needed)
            elif row.count(2) == 3 or column.count(2) == 3 or diagonal.count(2) == 3:
                result = 'Second player won'
                break
        gamepad.reverse() # reversing the gamepad to swing the diagonal
    # if there is no winner (result is empty - unchanged value), the result is Draw!:
    if result == '':
        result = 'Draw!'
    return result


print(tic_tac_toe(l1, l2, l3))
