from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []

    @property
    def guests(self):
        return sum([room.guests for room in self.rooms])

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f'{stars_count} stars Hotel')

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        room = next(filter(lambda r: room_number == r.number, self.rooms))
        room.take_room(people)

    def free_room(self, room_number: int):
        room = next(filter(lambda r: room_number == r.number, self.rooms))
        room.free_room()

    def status(self):
        free_rooms = ', '.join([str(r.number) for r in self.rooms if not r.is_taken])
        taken_rooms = ', '.join([str(r.number) for r in self.rooms if r.is_taken])
        return f'Hotel {self.name} has {self.guests} total guests\nFree rooms: {free_rooms}\nTaken rooms: {taken_rooms}'