from .booking import Booking
from .seats import Seat


class Room:
    def __init__(
            self, 
            title: str | None = None, 
            schedule: list[Booking] | None = None,
            seats: list[Seat] | None = None,
            autogenerate_seats: bool = True,
            saved: bool = False):
    
        if autogenerate_seats:
            seats = self._generate_seats()
        self.title = title
        self.seat = seats
        self.schedule = schedule
        self.saved = saved

    @staticmethod
    def from_database(room: dict):
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

    def _generate_seats(self, columns, rows) -> list[Seat]:
        pass