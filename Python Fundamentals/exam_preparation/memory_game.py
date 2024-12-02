def index_validation(sequence: list, indexes: list):
    i_1 = int(indexes[0])
    i_2 = int(indexes[1])
    if i_1 == i_2 or len(sequence) <= i_1 or len(sequence) <= i_2 or i_1 < 0 or i_2 < 0:
        return False, i_1, i_2
    return True, i_1, i_2


def move(sequence: list, indexes: list, moves_count: int):
    valid, i_1, i_2 = index_validation(sequence, indexes)
    if not valid:
        half_of_sequence = len(sequence) // 2
        sequence = sequence[:half_of_sequence] + [f'-{moves_count}a'] * 2 + sequence[half_of_sequence:]
        print('Invalid input! Adding additional elements to the board')
        return False, sequence
    if sequence[i_1] != sequence[i_2]:
        print('Try again!')
        return False, sequence
    print(f'Congrats! You have found matching elements - {sequence[i_1]}!')
    if i_1 < i_2:
        sequence.pop(i_2)
        sequence.pop(i_1)
    else:
        sequence.pop(i_1)
        sequence.pop(i_2)
    return True, sequence


def check_the_result(sequence: list):
    if len(sequence) > 0:
        print('Sorry you lose :(')
        return False
    return True


game_sequence = input().split()
command = input()
count = 0
won = False
while command != 'end':
    shot = command.split(' ')
    count += 1
    valid_move, game_sequence = move(game_sequence, shot, count)
    if len(game_sequence) > 0:
        command = input()
    else:
        won = True
        command = 'end'

if won:
    print(f"You have won in {count} turns!"'')
else:
    result = check_the_result(game_sequence)
    print(*game_sequence)