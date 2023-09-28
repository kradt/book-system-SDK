from book_system import Seat, Room


def test_getting_seat_by_it_id(sdk, created_room):
    seat = created_room.seats[0]
    seat_from_base = sdk.get(model=Seat, by_id=seat.id)
    assert seat_from_base
    assert seat_from_base.id == seat.id


def test_getting_seat_by_number(sdk, created_room):
    seat = created_room.seats[0]
    seat_from_base = sdk.get(Seat, by=Room, by_id=created_room.id, number=seat.number)
    assert seat_from_base
    assert seat_from_base.id == seat.id