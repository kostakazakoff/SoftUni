from collections import deque


def elf_makes_toy(capacity):
    global toys_maked, energy, eat_cookie, elf
    if elf < toy * capacity:
        elf *= 2
        elves.append(elf)
        return False
    toys_maked = capacity
    energy = toy * capacity
    eat_cookie = 1
    return True


elves = deque([int(x) for x in input().split()])
materials = [int(x) for x in input().split()]
used_energy = 0
toys_count = 0
work_count = 0

while materials and elves:
    elf = elves.popleft()
    toy = materials[-1]
    energy, toys_maked, eat_cookie = 0, 0, 0

    if elf < 5:
        continue

    work_count += 1

    if work_count % 3 == 0:
        elf_capacity = 2
    else:
        elf_capacity = 1

    if not elf_makes_toy(elf_capacity):
            continue

    if work_count % 5 == 0:
        if toys_maked:
            toys_maked = 0
            eat_cookie = 0

    elf -= energy
    toys_count += toys_maked
    used_energy += energy
    elves.append(elf + eat_cookie)
    materials.pop()

print(f"Toys: {toys_count}")
print(f"Energy: {used_energy}")

if elves: print(f"Elves left: {', '.join([str(x) for x in elves])}")
if materials: print(f"Boxes left: {', '.join([str(x) for x in materials])}")
