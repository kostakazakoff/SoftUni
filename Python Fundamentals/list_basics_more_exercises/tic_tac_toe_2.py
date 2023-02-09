import numpy as np

r1 = np.array(list(map(int, filter(lambda x: x != ' ', input()))))
r2 = np.array(list(map(int, filter(lambda x: x != ' ', input()))))
r3 = np.array(list(map(int, filter(lambda x: x != ' ', input()))))


def tic_tac_toe(row_1, row_2, row_3):
    result = ''
    a_winner = False

    gamepad = np.array([row_1, row_2, row_3], dtype=int)
    gamepad_reverse = gamepad[::-1]

    player_1 = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    player_2 = np.array([[2, 2, 2], [2, 2, 2], [2, 2, 2]])

    player1_diagonal = np.array([gamepad[a][a] == player_1[a][a] for a in range(3)]).all() or \
                       np.array([gamepad_reverse[a][a] == player_1[a][a] for a in range(3)]).all()
    player2_diagonal = np.array([gamepad[a][a] == player_2[a][a] for a in range(3)]).all() or \
                       np.array([gamepad_reverse[a][a] == player_2[a][a] for a in range(3)]).all()

    for i in range(3):
        player1_row = np.array([gamepad[i] == player_1[i]]).all()
        player2_row = np.array([gamepad[i] == player_2[i]]).all()
        player1_col = np.array([gamepad[:, i] == player_1[:, i]]).all()
        player2_col = np.array([gamepad[:, i] == player_2[:, i]]).all()

        if player1_row or player1_col or player1_diagonal:
            a_winner = True
            result = 'First player won'
            break
        elif player2_row or player2_col or player2_diagonal:
            a_winner = True
            result = 'Second player won'
            break

    if not a_winner:
        result = 'Draw!'
    return result


print(tic_tac_toe(r1, r2, r3))
