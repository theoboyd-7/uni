class CinemaTicket:

    max_price = 20.0

    def __init__(self, cust_name, title, price):
        self.customer_name = cust_name
        self.film_title = title
        self._price = float(price)

    @property
    def price(self):
        if self._price > self.max_price:
            self._price = self.max_price
        return self._price

    def apply_discount(self, percent):
        self._price = self._price * (1 - (percent / 100))

    def change_film(self, new_title):
        self.film_title = new_title

    def __str__(self):
        return f"{self.customer_name} - {self.film_title} - £{self.price:.2f}"
    

def test_cinema_ticket():
    ticket1 = CinemaTicket("Bob", "Avatar", 20.50)
    ticket2 = CinemaTicket("John", "Marvel", 8.75)

    print(ticket1)
    print(ticket2)

    ticket1.apply_discount(10)
    print(ticket1)

    ticket2.change_film("Avatar")
    print(ticket2)

test_cinema_ticket()