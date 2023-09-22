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
            body: dict | None = None,
            headers: dict | None = None,
            queries: dict | None = None) -> requests.Response:
        
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
        if not self._rooms:
            url = f"{self.api_url}/rooms/"
            self._rooms = [Room.from_json(room) for room in self._get(url)]
        return self._rooms

    @property
    def events(self) -> list[Event]:
        if not self._events:
            url = f"{self.api_url}/events/"
            self._events = [Event.from_json(event) for event in self._get(url)]
        return self._events
    
    def _get(self, url: str) -> dict:
        response = self._make_request(base_url=url, method="GET")
        json = response.json()
        if response.status_code != 200:
            raise ValueError(json["detail"])
        return json

    def get_room_by_id(self, room_id) -> Room:
        url = f"{self.api_url}/rooms/{room_id}/"
        json = self._get(url)
        return Room.from_json(json)

    def get_event_by_id(self, event_id) -> Event:
        url = f"{self.api_url}/events/{event_id}/"
        json = self._get(url)
        return Event.from_json(json)

    def get_booking_by_id(self, booking_id) -> Booking:
        url = f"{self.api_url}/rooms/{booking_id}/"
        json = self._get(url)
        return Booking.from_json(json)

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