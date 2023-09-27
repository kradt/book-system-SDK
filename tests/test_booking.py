import pytest
import datetime
from book_system import Booking, Event, Room


# Test creating a booking
def test_create_booking(booking, sdk):
    created_booking = sdk.create(booking)
    assert created_booking.id
    sdk.delete(created_booking)

# Test fetching a booking
def test_fetch_booking(created_booking, sdk):
    fetched_booking = sdk.get(model=Booking)
    assert int(fetched_booking.id) == int(created_booking.id)

# Test updating a booking
def test_update_booking(created_booking, sdk):
    now = datetime.datetime.now()
    created_booking.time_start = created_booking.time_start = now
    updated_booking = sdk.refresh(created_booking)
    assert updated_booking.time_start.hour == now.hour

# Test deleting a booking
def test_delete_booking(created_booking, sdk):
    sdk.delete(created_booking)
    deleted_booking = sdk.get(model=Booking)
    assert not deleted_booking

# Test listing all bookings
def test_list_bookings(created_booking, sdk):
    # Create multiple bookings
    event1 = Event(title="Event -1")
    event2 = Event(title="Event -2")
    room1 = Room(name="Room -1")
    room2 = Room(name="Room -2")

    event1 = sdk.create(event1)
    event2 = sdk.create(event2)
    room1 = sdk.create(room1)
    room2 = sdk.create(room2)

    booking1 = Booking(
        time_start=created_booking.time_start.replace(hour=14, minute=0),
        time_finish=created_booking.time_finish.replace(hour=15, minute=0),
        event=event1,
        room=room1,
    )
    booking2 = Booking(
        time_start=created_booking.time_start.replace(hour=15, minute=0),
        time_finish=created_booking.time_finish.replace(hour=16, minute=0),
        event=event2,
        room=room2,
    )

    booking1 = sdk.create(booking1)
    booking2 = sdk.create(booking2)

    # List all bookings
    bookings = sdk.booking
    assert len(bookings) >= 3  # At least the bookings we created

    sdk.delete(booking1)
    sdk.delete(booking2)
    sdk.delete(event1)
    sdk.delete(event2)
    sdk.delete(room1)
    sdk.delete(room2)

# Add more test cases as needed for other Booking actions
