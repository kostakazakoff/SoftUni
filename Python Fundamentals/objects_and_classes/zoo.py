class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, added_species, name):
        if added_species == 'mammal':
            self.mammals.append(name)
        elif added_species == 'fish':
            self.fishes.append(name)
        elif added_species == 'bird':
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species_in_zoo):
        output = ''
        if species_in_zoo == 'mammal':
            output += f'Mammals in {self.name}: {", ".join(self.mammals)}\n'
        elif species_in_zoo == 'fish':
            output += f'Fishes in {self.name}: {", ".join(self.fishes)}\n'
        elif species_in_zoo == 'bird':
            output += f'Birds in {self.name}: {", ".join(self.birds)}\n'
        output += f'Total animals: {Zoo.__animals}'
        return output


name_of_the_zoo = input()
zoo = Zoo(name_of_the_zoo)
number_of_species = int(input())

for _ in range(number_of_species):
    species, species_name = input().split()
    zoo.add_animal(species, species_name)

output_info = input()
print(zoo.get_info(output_info))