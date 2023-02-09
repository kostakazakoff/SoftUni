lost_fights = int(input())
helmet = float(input())
sword = float(input())
shield = float(input())
armor = float(input())
expenses = 0
shield_count = 0

for fight in range(1, lost_fights + 1):
    broken_helmet = False
    broken_sword = False
    if fight % 2 == 0:
        broken_helmet = True
        expenses += helmet
    if fight % 3 == 0:
        broken_sword = True
        expenses += sword
    if broken_sword and broken_helmet:
        expenses += shield
        shield_count += 1
        if shield_count % 2 == 0:
            expenses += armor

print(f'Gladiator expenses: {expenses:.2f} aureus')