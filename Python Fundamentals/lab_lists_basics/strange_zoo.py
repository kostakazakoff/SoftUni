animal = [input() for x in range(3)]
animal[0], animal[-1] = animal[-1], animal[0]
print(animal)