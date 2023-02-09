class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __repr__(self) -> str:
        return f'{self.name} {self.surname}'

    def __add__(self, other):
        return __class__(self.name, other.surname)


class Group:
    def __init__(self, name: str, people: list):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)
    
    def __add__(self, other):
        return __class__(f'{self.name} {other.name}', self.people + other.people)

    def __repr__(self):
        return f"Group {self.name} with members {', '.join(repr(p) for p in self.people)}"

    def __getitem__(self, idx):
        return f"Person {idx}: {self.people[idx]}"