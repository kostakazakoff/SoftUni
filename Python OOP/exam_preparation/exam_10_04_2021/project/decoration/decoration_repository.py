class DecorationRepository:
    def __init__(self):
        self.decorations = []

    def add(self, decoration):
        self.decorations.append(decoration)

    def remove(self, decoration):
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return True
        return False

    def find_by_type(self, decoration_type: str):
        decoration = next(filter(lambda x: x.__class__.__name__ == decoration_type, self.decorations), None)
        return decoration
