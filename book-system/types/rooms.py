from .booking import Booking
from .seats import Seat
from types import TypeModel


class Room(TypeModel):
    def __init__(
            self, 
            title: str | None = None, 
            schedule: list[Booking] | None = None,
            seats: list[Seat] | None = None,
            autogenerate_seats: bool = True):
        self.title = title
        self.seats = seats
        self.schedule = schedule
        self.autogenerate_seats = autogenerate_seats

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

    def to_dict(self) -> dict:
        seats_dict = [seat.to_dict() for seat in self.seats]
        booking_dict = [booking.to_dict() for booking in self.booking]
        return dict(
            title=self.title, 
            seats=seats_dict, 
            scheduler=booking_dict
        )