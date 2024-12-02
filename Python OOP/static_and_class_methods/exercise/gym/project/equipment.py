class Equipment:
    id = 1

    def __init__(self, name):
        self.name = name
        self.id = __class__.get_next_id()
        __class__.id = self.id + 1

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        return __class__.id