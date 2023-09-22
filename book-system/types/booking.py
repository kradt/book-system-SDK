import datetime

from types import TypeModel
from .events import Event
from .rooms import Room


class Booking(TypeModel):
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
