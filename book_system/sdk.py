import requests
from urllib.parse import urlencode
from typing import Literal

from .types import TypeModel
from .types.rooms import Room
from .types.events import Event
from .types.booking import Booking


class BookSystemSDK:
    def __init__(
            self,
            api_url: str,
            rooms: list[Room] | None = None,
            events: list[Event] | None = None):
        self.api_url = api_url
        self._rooms = rooms
        self._events = events

    def _make_request(
            url: str,
            method: Literal["GET", "POST", "PATCH", "DELETE"],
            body: dict | None = None,
            params: dict | None = None) -> dict:
        response = requests.request(method=method, url=url, json=body, params=params)
        json = response.json()
        if response.status_code not in [200, 201, 204]:
            raise json["detail"]
        return json
    
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

    def create(self, obj: TypeModel | list[TypeModel]):
        url = f"{self.api_url}{obj.base_url}"
        if isinstance(obj, list):
            return [o.from_json(self._create(url, body=o.body, params=o.params)) for o in obj]
        return obj.from_json(self._create(url, body=obj.body, params=obj.params))
    
    def refresh(self, obj: TypeModel | list[TypeModel]):
        obj = [obj] if not isinstance(obj, list) else obj
        [self.refresh(f"{self.api_url}{o.base_url}{o.id}", body={key: value for key, value in o.body.items() if value}, params=o.params) for o in obj]

    def delete(self, obj: TypeModel | list[TypeModel]):
        obj = [obj] if not isinstance(obj, list) else obj
        [self.refresh(f"{self.api_url}{o.base_url}{o.id}") for o in obj]

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
