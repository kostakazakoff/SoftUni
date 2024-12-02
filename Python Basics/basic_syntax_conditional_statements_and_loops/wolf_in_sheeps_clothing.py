s = input()
herd = s.split(', ')
herd.reverse()
sheep_in_danger_index = herd.index('wolf')
if herd.index('wolf') == 0:
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {sheep_in_danger_index}! You are about to be eaten by a wolf!")