import pytest
from book_system import Event

# Test creating an event
def test_create_event(event, sdk):
    created_event = sdk.create(event)
    assert created_event.id is not None
    assert created_event.params == {}
    sdk.delete(created_event)

# Test fetching an event
def test_fetch_event(created_event, sdk):
    fetched_event = sdk.get(model=Event)
    assert int(fetched_event.id) == int(created_event.id)


# Test deleting an event
def test_delete_event(created_event, sdk):
    sdk.delete(created_event)
    deleted_event = sdk.get(model=Event)
    assert not deleted_event

# Test listing all events
def test_list_events(created_event, sdk):
    # Create multiple events
    event1 = Event(title="Event 1")
    event2 = Event(title="Event 2")

    event1 = sdk.create(event1)
    event2 = sdk.create(event2)

    # List all events
    events = sdk.events
    assert len(events) >= 3  # At least the events we created
    sdk.delete(event1)
    sdk.delete(event2)

# Add more test cases as needed for other Event actions
