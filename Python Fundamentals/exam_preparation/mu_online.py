def potion_room(current_health: int, amount: int):
    if current_health + amount > 100:
        amount = 100 - current_health
        current_health = 100
    else:
        current_health += amount
    print(f'You healed for {amount} hp.')
    print(f'Current health: {current_health} hp.')
    return current_health


def chest_room(current_bitcoins: int, amount: int):
    current_bitcoins += amount
    print(f'You found {amount} bitcoins.')
    return current_bitcoins


def battle_room(monster: str, amount: int, current_health: int):
    current_health -= amount
    if current_health <= 0:
        print(f'You died! Killed by {monster}.')
        return True, current_health
    print(f'You slayed {monster}.')
    return False, current_health


health = 100
bitcoins = 0
rooms = []
room_inputs = input().split('|')

for room in room_inputs:
    action, value = room.split()
    rooms.append((action, int(value)))

for i in range(len(rooms)):
    action, points = rooms[i]
    if action == 'potion':
        health = potion_room(health, points)
    elif action == 'chest':
        bitcoins = chest_room(bitcoins, points)
    else:
        died, health = battle_room(action, points, health)
        if died:
            print(f'Best room: {i + 1}')
            break
else:
    print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")
