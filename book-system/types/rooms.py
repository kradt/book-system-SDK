from .booking import Booking
from .seats import Seat
from types import TypeModel


class Room(TypeModel):
    def __init__(
            self, 
            title: str | None = None, 
            schedule: list[Booking] | None = None,
            seats: list[Seat] | None = None,
            autogenerate_seats: bool = True,
            saved: bool = False):
        
        self.title = title
        self.seat = seats
        self.schedule = schedule
        self.autogenerate_seats = autogenerate_seats
        self.saved = saved

    @classmethod
    def from_database(cls, room: dict):
        """
            Getting room using json that we get from API
            TODO: add saved = True during adding it into the database
        """
        pass

    def book(self, booking: Booking):
        """
            Booking current room at passed time
        """
        pass

    def unbook(self, booking: Booking):
        """
            Unbook current rooom at passed time
        """

    def save(self):
        """
            Saving room into the database
            TODO: functionallity
        """
        if self.saved:
            raise ValueError("The room already saved in the database")
        self.saved = True
