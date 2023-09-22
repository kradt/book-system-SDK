from types.rooms import Room
from types.events import Event
from types.booking import Booking


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

    @property
    def events(self) -> list[Event]:
        return self._events
    
    def get_room_by_id(self, room_id) -> Room:
        pass

    def get_event_by_id(self, event_id) -> Event:
        pass

    def get_booking_by_id(self, booking_id) -> Booking:
        pass

    def create_room(room: Room) -> Room:
        pass

    def crete_event(event: Event) -> Event:
        pass

    def create_booking(booking: Booking) -> Booking:
        pass

    def delete_room(room: Room) -> None:
        pass

    def delete_event(event: Event) -> None:
        pass

    def delete_booking(booking: Booking) -> None:
        pass