class Guest:

    def __init__(self, name, loyalty_points):
        self.name = name
        self.loyalty_points = loyalty_points

    def __str__(self):
        return f"Guest: {self.name} ({self.loyalty_points} pts)"
    
class HotelRoom:

    def __init__(self, room_number, room_type, price):
        self.room_number = room_number
        self.room_type = room_type
        self.guest = None
        self.__price_per_night = price

    @property
    def price_per_night(self):
        return self.__price_per_night
    
    @price_per_night.setter
    def price_per_night(self, new_price):
        if new_price > 0:
            self.__price_per_night = new_price

    def check_in(self, guest):
        self.guest = guest
        print(self.guest)

    def __str__(self):
        if self.guest:
            return f"Room {self.room_number} ({self.room_type}) - Occupied by {self.guest.name}"
        return f"Room {self.room_number} is vacant"
    

def test_guest():
    guest = Guest("Theo", 1000)
    print(guest)

    room101 = HotelRoom(101, "Luxury", 1000)
    print(room101)
    room101.check_in(guest)
    print(room101)

    print(room101.price_per_night)
    room101.price_per_night = 1100
    print(room101.price_per_night)

test_guest()
        