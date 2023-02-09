from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish
from project.controller import Controller

controller = Controller()
plant = Plant()
decoration_repository = DecorationRepository()
fish_salt = SaltwaterFish('Nemo', 'Claun', 10)
fish_fresh = FreshwaterFish('Fresh', 'Som', 10)
controller.add_decoration('Plant')
print(controller.add_aquarium('SaltwaterAquarium', 'Black Sea'))
print(controller.add_aquarium('SaltwaterAquarium', 'Red Sea'))
print(controller.add_aquarium('Freshwater', 'Ropotamo'))
# print(controller.decorations_repository.decorations)
print(controller.add_decoration('Plant'))
print(controller.add_decoration('Plant'))
print(controller.decorations_repository.decorations)
print()
print(controller.insert_decoration('Black Sea', 'Ornament'))
print(controller.insert_decoration('Black Sea', 'Plant'))
print(controller.insert_decoration('Black Sea', 'Plant'))
print(controller.decorations_repository.decorations)
print()
print(controller.aquariums[0])

# print()
# print(controller.add_fish('Black Sea', 'FreshwaterFish', 'Som', 'sladkovodna', 10))
# controller.add_fish('Black Sea', 'SaltwaterFish', 'Nemo', 'Claun', 10)

# print()
# print(controller.feed_fish('Black Sea'))
# print(controller.calculate_value('Black Sea'))
# print()
# print(controller.report())

