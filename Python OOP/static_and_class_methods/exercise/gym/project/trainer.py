class Trainer:
    id = 1

    def __init__(self, name):
        self.name = name
        self.id = Trainer.get_next_id()
        Trainer.id = self.id + 1

    def __repr__(self) -> str:
        return f"Trainer <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Trainer.id