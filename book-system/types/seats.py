

class Seat:
    def __init__(
            self,
            row: int,
            column: int,
            number: int,
            booked: bool = False,
            additional_data: dict | None = None,
            saved: bool = False,
            room_id: int | None = None):
        self.row = row
        self.column = column
        self.number = number
        self.booked = booked
        self.additional_data = additional_data
        self.saved = saved
        self.room_id = room_id

    @staticmethod
    def from_database(self, seat: dict):
        """
            Getting seat using json that we get from API
        """
        pass

    @property
    def room(self):
        """
            TODO: Getting room by it id in the database and return it
        """
        pass

    def book(self):
        """
            TODO: booking seat in the database
        """
        if self.booked:
            raise ValueError("The seat have already booked")
        self.booked = True
        pass

    def unbook(self, strict: bool = False):
        """
            TODO: unbooking seat in the database
        """
        self.booked = False
        pass

    def save(self):
        """
            Save Seat into the database
        """
        pass