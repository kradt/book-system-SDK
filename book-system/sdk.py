from types.rooms import Room
from types.events import Event


class BookSystemSDK:
    def __init__(
            self,
            api_url: str,
            rooms: list[Room] | None = None,
            events: list[Event] | None = None):
        self.api_url = api_url
        self._rooms = rooms
        self.events = events

    @property
    def rooms(self) -> list[Room]:
        return self._rooms
    
    @rooms.setter
    def rooms(self, rooms: list) -> None:
        self._rooms = rooms

    @property
    def events(self) -> list[Event]:
        return self._events
    
    @events.setter
    def events(self, events) -> None:
        self._events = events