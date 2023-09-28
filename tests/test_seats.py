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


def test_update_seat_by_id(sdk, created_room):
    seat = created_room.seats[0]
    seat.booked = True
    refreshed_seat = sdk.refresh(seat)
    assert refreshed_seat
    assert refreshed_seat.booked != False


def test_create_room_with_seats(sdk):
    seat1 = Seat(row=1, column=1, number=1, booked=False, additional_data={"price": 2000})
    seat2 = Seat(row=1, column=2, number=2, booked=False, additional_data={"price": 5000})
    room = Room(name="NewRoom", seats=[seat1, seat2])
    room = sdk.create(room)
    assert room.seats[1].id
    assert len(sdk.rooms) == 1
    assert len(room.seats) == 2
    assert room.seats[0].number == seat1.number
    assert room.seats[0].body == seat1.body
    assert room.seats[0].params == seat1.params
    sdk.delete(room)