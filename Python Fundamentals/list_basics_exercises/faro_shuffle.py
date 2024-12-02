deck_of_cards = input().split()
shuffles = int(input())

for s in range(shuffles):
    half_of_cards = len(deck_of_cards) // 2
    top_half = deck_of_cards[:half_of_cards]
    bottom_half = deck_of_cards[half_of_cards:]
    deck_of_cards.clear()
    for card in range(len(top_half)):
        deck_of_cards.append(top_half[card])
        deck_of_cards.append(bottom_half[card])

print(deck_of_cards)
