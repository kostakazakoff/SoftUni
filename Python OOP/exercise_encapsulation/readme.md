# Wild Cat Zoo
Create a separate file for each class as shown below and submit a zip file containing all files (zip the whole project folder/module) - it is important to include all files in the project module to make proper imports.

![image](https://user-images.githubusercontent.com/104040753/200065231-87dd47a4-80ff-4219-abf7-e59cc7c1db71.png)

The Animal class is a base class for any type of animal in the zoo. It should receive four public attributes - a name (string), a gender (str), an age (int), and a money_for_care (int) upon initialization.

The Animal class should also have 1 additional method:
- __repr__() - returns string representation of the animal in the format: "Name: {name}, Age: {age}, Gender: {gender}"

The Lion, the Tiger, and the Cheetah classes should inherit from the Animal class. Each of these animals costs a certain amount of money to be cared for:
- A lion needs 50
- A tiger needs 45
- A cheetah needs 60

The Worker class is a base class for any type of employee in the zoo. It should receive three public attributes - a name (string), an age (int), and a salary (int) upon initialization.

The Worker class should also have one method:
- __repr__() - returns string representation of the workers in the format: "Name: {name}, Age: {age}, Salary: {salary}"
The Keeper, the Caretaker, and the Vet classes should inherit from the Worker class.
The Zoo class should receive 4 attributes upon initialization:
- Public attribute name: string
- Private attribute budget: int
- Private attribute animal_capacity: int
- Private attribute workers_capacity: int
It should also have 2 instance attributes:
- Public attribute animals: list - (empty upon initialization)
- Public attribute workers: list - (empty upon initialization)
The Zoo class should also have 8 methods:
- add_animal(animal, price)
    - If you have enough budget and capacity add the animal (instance of Lion/Tiger/Cheetah) to the animals' list, reduce the budget, and return "{name} the {type of animal (Lion/Tiger/Cheetah)} added to the zoo"
    - If you have the capacity, but no budget, return "Not enough budget"
    - In any other case, you do not have space, and you should return "Not enough space for animal"
- hire_worker(worker)
    - If you have not exceeded the capacity of workers in the zoo for the worker (instance of Keeper/Caretaker/Vet), add him to the workers and return "{name} the {type(Keeper/Vet/Caretaker)} hired successfully"
    - Otherwise, return "Not enough space for worker"
- fire_worker(worker_name)
    - If there is a worker with that name in the workers' list, remove him and return "{worker_name} fired successfully"
    - Otherwise, return "There is no {worker_name} in the zoo"
- pay_workers()
    - If you have enough budget to pay the workers (sum their salaries) pay them and return "You payed your workers. They are happy. Budget left: {left_budget}"
    - Otherwise, return "You have no budget to pay your workers. They are unhappy"
- tend_animals()
    - If you have enough budget to take care of the animals, reduce the budget and return "You tended all the animals. They are happy. Budget left: {left_budget}"
    - Otherwise, return "You have no budget to tend the animals. They are unhappy."
- profit(amount)
    - Increase the budget with the given amount of profit
- animals_status()
    - Returns the following string (Hint: use the __repr__ methods of the animals to print them on the console):

        "You have {total_animals_count} animals

        ----- {amount_of_lions} Lions:

        {lion1}

        …
        
        {lionN}
        
        ----- {amount_of_tigers} Tigers:
        
        {tiger1}
        
        …
        
        {tigerN}
        
        ----- {amount_of_cheetahs} Cheetahs:
        
        {cheetah1}
        
        …
        
        {cheetahN}"

- workers_status()
    - Returns the following string (Hint: use the __repr__ methods of the workers to print them on the console):
    
        "You have {total_workers_count} workers
        
        ----- {amount_of_keepers} Keepers:
        
        {keeper1}
        
        …
        
        {keeperN}
        
        ----- {amount_of_caretakers} Caretakers:
        
        {caretaker1}
        
        …
        
        {caretakerN}
        
        ----- {amount_of_vetes} Vets:
        
        {vet1}
        
        …
        
        {vetN}"


# Pizza Maker
Create a separate file for each class as shown below and submit a zip file containing all files (zip the whole project folder/module) - it is important to include all files in the project module to make proper imports.

![image](https://user-images.githubusercontent.com/104040753/200066000-7512a193-6ae0-45a7-a7e4-6b4215997550.png)

Create a class called Topping. Upon initialization, it should receive:
- topping_type: str - if the topping is an empty string, raise a ValueError with the message "The topping type cannot be an empty string"
- weight: float - if the weight is 0 or less, raise a ValueError with the message "The weight cannot be less or equal to zero"

Hint: Use Getters and Setters.

Create a class called Dough. Upon initialization, it should receive:
- flour_type: str - if the flour type is an empty string, raise a ValueError with the message "The flour type cannot be an empty string"
- baking_technique: str - if the technique is an empty string, raise a ValueError with the message "The baking technique cannot be an empty string"
- weight: float - if the weight is 0 or less, raise a ValueError with the message "The weight cannot be less or equal to zero"

Create a class called Pizza. Upon initialization, it should receive:
- name: str - if the name is an empty string, raise a ValueError with the message "The name cannot be an empty string"
- dough: Dough - if the dough is None, raise a ValueError with the message "You should add dough to the pizza"
toppings_capacity: int – represents the maximum number of toppings the pizza should have. If the capacity is 0 or less, raise a ValueError with the message "The topping's capacity cannot be less or equal to zero"
- toppings: dict – empty dictionary upon initialization that will contain the topping type as a key and the topping's weight as a value.

The class should also have 2 instance methods:
- add_topping(topping: Topping) 
    - Add a new topping to the dictionary
    - If there is no space left for a new topping, raise a ValueError: "Not enough space for another topping"
    - If the topping is already in the dictionary, increase the value of its weight.
- calculate_total_weight() - returns the total weight of the pizza (dough's weight and toppings' weight)


# Football Team Generator
Create a separate file for each class as shown below and submit a zip file containing all files (zip the whole project folder/module) - it is important to include all files in the project module to make proper imports.

Create a class called Player. Upon initialization, it should receive:
- Private attribute name: string
- Private attribute sprint: int
- Private attribute dribble: int
- Private attribute passing: int
- Private attribute shooting: int

You should create property only for the name of the player. The class should also have one additional method:
- Override the __str__() method of the class so it returns:
    > "Player: {name}
    >
    > Sprint: {sprint}
    >
    > Dribble: {dribble}
    >
    > Passing: {passing}
    >
    > Shooting: {shooting}"

Create a class called Team. Upon initialization, it should receive:
- Private attribute name: string
- Private attribute rating: int

The class should also have a private instance attribute - players: list - empty list upon initialization that will contain all - the players (objects)

The Team class have the following methods:
- add_player(player: Player)
    - If the player is already in the team, return "Player {name} has already joined"
    - Otherwise, add the player to the team and return "Player {name} joined team {team_name}"
- remove_player(player_name: str)
    - Remove the player and return him
    - If the player is not in the team, return "Player {player_name} not found"


# Restaurant
Create a restaurant with the following classes and hierarchy:

![image](https://user-images.githubusercontent.com/104040753/200067521-7ac2d2ba-6870-4409-9b51-89c0f491c764.png)

Submit in judge a zip file containing a separate file for each of the classes using the structure shown below:

![image](https://user-images.githubusercontent.com/104040753/200067549-c3d8cbdc-e380-49e0-a001-7a5eaa9728a3.png)

The Product class should have the following private attributes and subsequent getters:
- name: string
- price: float

Beverage and Food classes are products:
- The Beverage class should have an additional private attribute – milliliters: float and its subsequent getter
- The Food class should have an additional private attribute – grams: float and its subsequent getter

HotBeverage and ColdBeverage are beverages.
Coffee and Tea are hot beverages:
- The Coffee class should have an additional private attribute – caffeine: float and its subsequent getter. It should also have the following class attributes, which should apply to all coffees made:
    - MILLILITERS = 50 (constant)
    - PRICE = 3.50 (constant)

Starter, MainDish, and Dessert are food: 
- The Dessert class should have an additional private attribute - calories - float and its subsequent getter

Salmon is a main dish. Also, it must have the following class attribute, which should apply to all salmons:
- GRAMS = 22 (constant)

Soup is a starter.
Cake is a dessert. Also, it must have the following class attributes which should apply to all cakes made:
- GRAMS = 250 (constant)
- CALORIES = 1000 (constant)
- PRICE = 5 (constant)
