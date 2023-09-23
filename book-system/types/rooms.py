from .booking import Booking
from .seats import Seat
from types import TypeModel


class Room(TypeModel):
    def __init__(
            self, 
            name: str | None = None, 
            schedule: list[Booking] | None = None,
            seats: list[Seat] | None = None,
            autogenerate_seats: bool = True):
        self.name = name
        self.seats = seats
        self.schedule = schedule
        self.autogenerate_seats = autogenerate_seats

    @classmethod
    def from_json(cls, room: dict):
        """
            Getting room using json that we get from API
        """
        seats = [Seat.from_json(seat) for seat in room["seats"]]
        return super.__init__(name=room["name"], seats=seats)

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
