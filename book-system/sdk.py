import requests
from urllib.parse import urlencode
from typing import Literal

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

    def _make_request(
            base_url: str,
            method: Literal["GET", "POST", "PATCH", "DELETE"] = "GET", 
            headers: dict | None = None,
            body: dict | None = None,
            queries: dict | None = None):
        
        url = f"{base_url}?{urlencode(queries)}"
        if method == "GET":
            request = requests.get(url)
        elif method == "POST":
            request = requests.post(url, data=body, headers=headers)
        elif method == "DELETE":
            request = requests.delete(url, headers=headers)
        elif method == "PATCH":
            request = requests.patch(url, data=body, headers=headers)        
        return request
    
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