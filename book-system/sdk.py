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
        self._events = events

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
    
    def _get(self, url: str) -> dict:
        response = self._make_request(base_url=url, method="GET")
        json = response.json()
        if response.status_code != 200:
            raise ValueError(json["detail"])
        return json
    
    def _delete(self, url: str) -> None:
        response = self._make_request(base_url=url, method="DELETE")
        if response.status_codes != 204:
            json = response.json()
            raise ValueError(json["detail"])
        
    def _craete_(self, url: str, body: dict):
        response = self._make_request(base_url=url, method="POST", body=body)
        json = response.json()
        if response.status_code != 201:
            raise ValueError(json["detail"])
        return json

    def _refresh(self, url: str, body: dict):
        response = self._make_request(base_url=url, method="PATCH", body=body)
        json = response.json()
        if response.status_code != 200:
            raise ValueError(json["detail"])
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

    def create_room(self, room: Room) -> Room:
        url = f"{self.api_url}/rooms/"
        body = room.to_dict()
        return Room.from_json(self._craete_(url, body=body))

    def create_event(self, event: Event) -> Event:
        url = f"{self.api_url}/events/"
        body = event.to_dict()
        return Event.from_json(self._craete_(url, body=body))

    def create_booking(self, booking: Booking) -> Booking:
        url = f"{self.api_url}/booking/"
        body = booking.to_dict()
        return Booking.from_json(self._craete_(url, body=body))

    def refresh_room(self, room: Room) -> Room:
        url = f"{self.api_url}/rooms/{room.id}"
        room = room.to_dict()
        body = dict(name=room["title"], seats=room["seats"])
        return Room.from_json(self._refresh(url, body=body))

    def refresh_event(self, event: Event) -> Event:
        url = f"{self.api_url}/events/{event.id}"
        event = event.to_dict()
        return Event.from_json(self._refresh(url, body=event))

    def refresh_booking(self, booking: Booking) -> Booking:
        url = f"{self.api_url}/booking/{booking.id}"
        booking = booking.to_dict()
        body = dict(
            time_start=booking["time_start"], 
            time_finish=booking["time_finish"],
            additional_data=booking["additional_data"]
        )
        return Booking.from_json(self._refresh(url, body=body))

    def delete_room_by_id(self, room_id: int) -> None:
        url = f"{self.api_url}/rooms/{room_id}"
        self._delete(url)

    def delete_event_by_id(self, event_id: int) -> None:
        url = f"{self.api_url}/events/{event_id}"
        self._delete(url)

    def delete_booking_by_id(self, booking_id: int) -> None:
        url = f"{self.api_url}/booking/{booking_id}"
        self._delete(url)
