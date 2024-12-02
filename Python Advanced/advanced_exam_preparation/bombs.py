from collections import deque


bombs = {
        60: {'name': 'Cherry Bombs', 'amount': 0},
        40: {'name': 'Datura Bombs', 'amount': 0},
        120: {'name': 'Smoke Decoy Bombs', 'amount': 0}}

bomb_effects = deque([int(x) for x in input().split(', ')])
bomb_casings = [int(x) for x in input().split(', ')]
bomb_pouch_filled = False

while bomb_effects and bomb_casings:
    bomb = bomb_effects[0] + bomb_casings[-1]
    if bomb not in bombs:
        bomb_casings[-1] -= 5
        continue

    bomb_effects.popleft()
    bomb_casings.pop()

    bombs[bomb]['amount'] += 1

    if all([x['amount'] >= 3 for x in bombs.values()]):
        bomb_pouch_filled = True
        break

if bomb_pouch_filled: print("Bene! You have successfully filled the bomb pouch!")
else: print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects: print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effects])}")
else: print("Bomb Effects: empty")

if bomb_casings: print(f"Bomb Casings: {', '.join([str(x) for x in bomb_casings])}")
else: print("Bomb Casings: empty")

[print(f"{bomb['name']}: {bomb['amount']}") for bomb in bombs.values()]