def battle(current_energy: int, battle_energy: int):
    current_energy -= battle_energy
    if current_energy < 0:
        current_energy = 0
    return current_energy


energy = int(input())
command = input()
won_battles = 0
not_enough_energy = False

while command != 'End of battle':
    distance = int(command)
    if energy < distance:
        not_enough_energy = True
        break
    energy = battle(energy, distance)
    won_battles += 1
    if won_battles % 3 == 0:
        energy += won_battles
    command = input()
else:
    print(f'Won battles: {won_battles}. Energy left: {energy}')

if not_enough_energy:
    print(f'Not enough energy! Game ends with {won_battles} won battles and {energy} energy')
