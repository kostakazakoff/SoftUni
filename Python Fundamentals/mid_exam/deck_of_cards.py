def card_is_the_in_deck(deck_of_cards: list, card_name: str):
    if card_name in deck_of_cards:
        return True
    return False


def valid_card_index(deck_of_cards: list, card_index: int):
    if 0 <= card_index < len(deck_of_cards):
        return True
    return False


def add_card(deck_of_cards: list, card_name: str):
    if card_is_the_in_deck(deck_of_cards, card_name):
        print('Card is already in the deck')
        return deck_of_cards
    deck_of_cards.append(card_name)
    print('Card successfully added')
    return deck_of_cards


def remove_card(deck_of_cards: list, card_name: str):
    if not card_is_the_in_deck(deck_of_cards, card_name):
        print('Card not found')
        return deck_of_cards
    deck_of_cards.remove(card_name)
    print('Card successfully removed')
    return deck_of_cards


def remove_card_on_position(deck_of_cards: list, position: int):
    if not valid_card_index(deck_of_cards, position):
        print('Index out of range')
        return deck_of_cards
    deck_of_cards.pop(position)
    print('Card successfully removed')
    return deck_of_cards


def insert_card(deck_of_cards: list, position: int, card_name: str):
    if not valid_card_index(deck_of_cards, position):
        print('Index out of range')
        return deck_of_cards
    if card_is_the_in_deck(deck_of_cards, card_name):
        print('Card is already added')
        return deck_of_cards
    deck_of_cards.insert(position, card_name)
    print('Card successfully added')
    return deck_of_cards


deck = input().split(', ')
number_of_commands = int(input())

for _ in range(number_of_commands):
    command = input().split(', ')
    action = command[0]

    if action == 'Add':
        card = command[1]
        deck = add_card(deck, card)
    elif action == 'Remove':
        card = command[1]
        deck = remove_card(deck, card)
    elif action == 'Remove At':
        index = int(command[1])
        deck = remove_card_on_position(deck, index)
    elif action == 'Insert':
        index = int(command[1])
        card = command[2]
        deck = insert_card(deck, index, card)

print(', '.join(deck))