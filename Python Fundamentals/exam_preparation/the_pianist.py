def validation(pieces_dict: dict, piece_to_check: str):
    if piece_to_check in pieces_dict:
        return True
    return False


def add_piece(pieces_dict: dict, piece_to_add: str, composer: str, key_to_add: str):
    piece_exist = validation(pieces_dict, piece_to_add)
    if piece_exist:
        print(f'{piece_to_add} is already in the collection!')
        return pieces_dict
    pieces_dict.update({piece: [composer, key_to_add]})
    print(f'{piece_to_add} by {composer} in {key_to_add} added to the collection!')
    return pieces_dict


def remove_piece(pieces_dict: dict, piece_to_remove: str):
    piece_exist = validation(pieces_dict, piece_to_remove)
    if not piece_exist:
        print(f'Invalid operation! {piece_to_remove} does not exist in the collection.')
        return pieces_dict
    del pieces_dict[piece_to_remove]
    print(f'Successfully removed {piece_to_remove}!')
    return pieces_dict


def change_key(pieces_dict: dict, piece_to_change: str, new_key: str):
    piece_exist = validation(pieces_dict, piece_to_change)
    if not piece_exist:
        print(f'Invalid operation! {piece_to_change} does not exist in the collection.')
        return pieces_dict
    pieces_dict[piece_to_change][1] = new_key
    print(f'Changed the key of {piece_to_change} to {new_key}!')
    return pieces_dict


def output(pieces_dict: dict):
    for piece_name, content in pieces_dict.items():
        print(f'{piece_name} -> Composer: {content[0]}, Key: {content[1]}')


number_of_pieces = int(input())
pieces = {}
for _ in range(number_of_pieces):
    piece, author, key = input().split('|')
    pieces.update({piece: [author, key]})

command = input()
while command != 'Stop':
    command = command.split('|')
    action = command[0]
    piece = command[1]
    if action == 'Add':
        author = command[2]
        key = command[3]
        pieces = add_piece(pieces, piece, author, key)
    elif action == 'Remove':
        pieces = remove_piece(pieces, piece)
    else:
        key = command[2]
        pieces = change_key(pieces, piece, key)

    command = input()

output(pieces)
