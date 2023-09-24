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
    
    def create(self, obj: TypeModel) -> TypeModel:
        url = f"{self.api_url}{obj.base_url}"
        return obj.from_json(self._make_request(url, method="POST", body=obj.body, params=obj.params))
    
    def refresh(self, obj: TypeModel) -> TypeModel:
        url = f"{self.api_url}{obj.base_url}{obj.id}"
        return obj.from_json(self._make_request(url=url, method="PATCH", body=obj.body, params=obj.params))

    def delete(self, obj: TypeModel | list[TypeModel]):
        url = f"{self.api_url}{obj.base_url}{obj.id}"
        self._make_request(url=url, method="DELETE")

    def get_by_id(self, model, id) -> TypeModel:
        url = f"{self.api_url}{model.base_url}{id}"
        json = self._make_request(url, method="GET")
        return model.from_json(json)
