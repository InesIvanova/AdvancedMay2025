from project.room import Room

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms: list[Room] = []
        self.capacity = 0

    @property
    def guests(self):
        return sum([r.guests for r in self.rooms])

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def get_room(self, room_numer):
        return [r for r in self.rooms if r.number == room_numer][0]
        # return next([r for r in self.rooms if r.number == room_numer])

    def take_room(self, room_number, people):
        room = self.get_room(room_number)
        result = room.take_room(people)


    def free_room(self, number):
        room = self.get_room(number)
        result = room.free_room()

    def status(self):
        free_rooms = [str(r.number) for r in self.rooms if not r.is_taken]
        taken_rooms = [str(r.number) for r in self.rooms if r.is_taken]

        return f"Hotel {self.name} has {self.guests} total guests\nFree rooms: {', '.join(free_rooms)}\nTaken rooms: {', '.join(taken_rooms)}"
