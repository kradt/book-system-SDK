import pytest
import datetime
from book_system import Room, Event, Booking, Seat
from book_system import BookSystemSDK


@pytest.fixture(scope="function")
def room(sdk):
    room = Room(name="Test Room", autogenerate_seats=True, columns=2, rows=2)
    yield room


@pytest.fixture(scope="function")
def created_room(sdk, room):
    new_room = sdk.create(room)
    yield new_room
    try:
        sdk.delete(new_room)
    except ValueError:
        pass


@pytest.fixture
def event(sdk):
    event = Event(title="Some Title")
    yield event


@pytest.fixture
def created_event(sdk, event):
    new_event = sdk.create(event)
    yield new_event
    try:
        sdk.delete(new_event)
    except ValueError:
        pass


@pytest.fixture
def booking(sdk, created_event, created_room):
    book = Booking(time_start=datetime.datetime.now(), time_finish=datetime.datetime.now(), event=created_event, room=created_room)
    yield book


@pytest.fixture(scope="function")
def created_booking(sdk, booking):
    new_book = sdk.create(booking)
    yield new_book
    try:
        sdk.delete(new_book)
    except ValueError:
        pass


@pytest.fixture
def sdk():
    yield BookSystemSDK(api_url="http://localhost:5000")
