from .seats import Seat
from . import TypeModel


class Room(TypeModel):
    def __init__(
            self, 
            name: str | None = None, 
            seats: list[Seat] | None = None,
            autogenerate_seats: bool = False, 
            columns: int | None = None,
            rows: int | None = None):
        
        if autogenerate_seats and (not columns or not rows):
            raise ValueError("If u wanna use autogenerate you should pass number of columns and rows")
        self.name = name
        self.columns = columns
        self.rows = rows
        self.seats = seats
        self.autogenerate_seats = autogenerate_seats

    @classmethod
    def from_json(cls, room: dict):
        """
            Getting room using json that we get from API
        """
        seats = room.get("seats")
        seats = [Seat.from_json(seat) for seat in seats] if seats else None
        return cls(name=room["name"], seats=seats)

    def to_dict(self) -> dict:
        seats_dict = [seat.to_dict() for seat in self.seats] if self.seats else None
        return dict(
            name=self.name, 
            seats=seats_dict
        )
