from collections import deque


effects = deque([int(x) for x in input().split(', ')])
explosives = [int(x) for x in input().split(', ')]
fireworks = {'Palm Fireworks': 0, 'Willow Fireworks': 0, 'Crossette Fireworks': 0}
perfect_show = False

while effects and explosives:
    if effects[0] <= 0:
        effects.popleft()
        continue
    if explosives[-1] <= 0:
        explosives.pop()
        continue

    effect, explsv = effects.popleft(), explosives[-1]
    mix = effect + explsv

    if mix % 15 == 0:
        fireworks['Crossette Fireworks'] += 1
        explosives.pop()

    elif mix % 3 == 0:
        fireworks['Palm Fireworks'] += 1
        explosives.pop()

    elif mix % 5 == 0:
        fireworks['Willow Fireworks'] += 1
        explosives.pop()

    else:
        effects.append(effect - 1)

    perfect_show = all((
        fireworks['Palm Fireworks'] > 2,
        fireworks['Willow Fireworks'] > 2,
        fireworks['Crossette Fireworks'] > 2))

    if perfect_show:
        break

if perfect_show: print("Congrats! You made the perfect firework show!")
else: print("Sorry. You can't make the perfect firework show.")

if effects: print(f"Firework Effects left: {', '.join(str(x) for x in effects)}")
if explosives: print(f"Explosive Power left: {', '.join(str(x) for x in explosives)}")

[print(f"{k}: {v}") for k, v in fireworks.items()]

