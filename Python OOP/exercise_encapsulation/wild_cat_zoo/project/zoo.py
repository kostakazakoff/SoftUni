class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals, self.workers = [], []

    def add_animal(self, animal, price):
        if price > self.__budget:
            return "Not enough budget"
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        

    def fire_worker(self, worker_name):
        try:
            worker = next(filter(lambda w: w.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"
        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        workers_total_salary = sum(w.salary for w in self.workers)
        if self.__budget < workers_total_salary:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= workers_total_salary
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        animals_total_needs = sum(a.money_for_care for a in self.animals)
        if self.__budget < animals_total_needs:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= animals_total_needs
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        animals = {'Lion': [], 'Tiger': [], 'Cheetah': []}
        [animals[animal.__class__.__name__].append(str(animal)) for animal in self.animals]

        output = [f'You have {len(self.animals)} animals']

        for animal_class, animal_names in animals.items():
            output.append(f'----- {len(animal_names)} {animal_class}s:\n' + '\n'.join(animal_names))
        return '\n'.join(output)

    def workers_status(self):
        workers = {'Keeper': [], 'Caretaker': [], 'Vet': []}
        [workers[worker.__class__.__name__].append(str(worker)) for worker in self.workers]

        output = [f'You have {len(self.workers)} workers']

        for worker_class, worker_names in workers.items():
            output.append(f'----- {len(worker_names)} {worker_class}s:\n' + '\n'.join(worker_names))
        return '\n'.join(output)
