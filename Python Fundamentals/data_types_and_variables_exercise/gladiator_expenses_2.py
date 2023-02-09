lost_fights = int(input())
helmet = float(input())
sword = float(input())
shield = float(input())
armor = float(input())
expenses = 0
shield_count = 0

broken_helmet = lost_fights // 2
broken_sword = lost_fights // 3
broken_shield = lost_fights // 6
broken_armor = broken_shield // 2
expenses += broken_helmet * helmet + \
    broken_sword * sword + \
    broken_shield * shield + \
    broken_armor * armor

print(f'Gladiator expenses: {expenses:.2f} aureus')
