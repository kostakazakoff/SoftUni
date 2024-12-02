def validation(piece_to_check: str):
    if piece_to_check in pieces:
        return True


def add_piece(piece_to_add: str, composer: str, key_to_add: str):
    piece_exist = validation(piece_to_add)
    if piece_exist:
        print(f'{piece_to_add} is already in the collection!')
        return
    pieces.update({piece: [composer, key_to_add]})
    print(f'{piece_to_add} by {composer} in {key_to_add} added to the collection!')


def remove_piece(piece_to_remove: str):
    piece_exist = validation(piece_to_remove)
    if not piece_exist:
        print(f'Invalid operation! {piece_to_remove} does not exist in the collection.')
        return
    del pieces[piece_to_remove]
    print(f'Successfully removed {piece_to_remove}!')
    return


def change_key(piece_to_change: str, new_key: str):
    piece_exist = validation(piece_to_change)
    if not piece_exist:
        print(f'Invalid operation! {piece_to_change} does not exist in the collection.')
        return
    pieces[piece_to_change][1] = new_key
    print(f'Changed the key of {piece_to_change} to {new_key}!')
    return


def output():
    for piece_name, content in pieces.items():
        print(f'{piece_name} -> Composer: {content[0]}, Key: {content[1]}')


number_of_pieces = int(input())
pieces = {}

for _ in range(number_of_pieces):
    piece, author, key = input().split('|')
    pieces.update({piece: [author, key]})

command = input()
while command != 'Stop':
    action, piece, *author_key = command.split('|')
    if action == 'Add':
        author, key = author_key
        add_piece(piece, author, key)
    elif action == 'Remove':
        remove_piece(piece)
    else:
        key = author_key[0]
        change_key(piece, key)

    command = input()

output()
