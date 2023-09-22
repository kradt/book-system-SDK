import datetime

from .events import Event
from .rooms import Room


class Booking:
    def __init__(
            self, 
            event: Event,
            room: Room,
            time_from: datetime.datetime,
            time_to: datetime.datetime):
        self.event = event
        self.room = room
        self.time_from = time_from
        self.time_to = time_to


    def save(self, booking: dict):
        """
            TODO: saving booking in the database
        """
        pass