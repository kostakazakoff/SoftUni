from project.rooms.room import Room


class Everland:

    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        hotel_monthly_consumption = sum(room.monthly_total_consumption for room in self.rooms)
        return f"Monthly consumption: {hotel_monthly_consumption:.2f}$."

    def pay(self):
        output = []
        for room in self.rooms:
            bill = room.monthly_total_consumption
            if room.budget < bill:
                output.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.remove(room)
            else:
                room.budget -= bill
                output.append(f"{room.family_name} paid {bill:.2f}$ and have {room.budget:.2f}$ left.")
                
        return '\n'.join(output)

    def status(self):
        output = [f'Total population: {sum(r.members_count for r in self.rooms)}']
        for room in self.rooms:
            output.append(room.__repr__())
            
        return '\n'.join(output)
