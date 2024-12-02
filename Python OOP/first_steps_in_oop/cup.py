class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, quantity):
        if self.size >= self.quantity + quantity:
            self.quantity += quantity

    def status(self):
        free_space = self.size - self.quantity
        return free_space