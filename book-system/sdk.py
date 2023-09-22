

class BookSystemSDK:
    def __init__(self, api_url, rooms: list | None = None, events: list | None = None):
        self.api_url = api_url
        self._rooms = rooms
        self.events = events

    @property
    def rooms(self):
        return self._rooms
    
    @rooms.setter
    def rooms(self, rooms: list):
        self._rooms = rooms

    @property
    def events(self):
        return self._events
    
    @events.setter
    def events(self, events):
        self._events = events