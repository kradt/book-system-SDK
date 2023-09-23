import datetime

from . import TypeModel
from .events import Event
from .rooms import Room


class Booking(TypeModel):
    def __init__(
            self, 
            event: Event,
            room: Room,
            time_start: datetime.datetime,
            time_finish: datetime.datetime, 
            additional_data: dict| None = None):
        self.event = event
        self.room = room
        self.time_start = time_start
        self.time_finish = time_finish
        self.additional_data = additional_data

    @classmethod
    def from_json(cls, booking: dict):
        pass

    def to_dict(self):
        """
            It can cause error when room or event didn't save in the database
        """
        return dict(
            time_start=self.time_start,
            time_finish=self.time_finish, 
            additional_data=self.additional_data,
            room_id=self.room.id,
            event_id=self.event.id)
