class CoffeeShop:

    def __init__(self):
        self.customers = []

    def add_customer(self, name):
        self.customers.append(name)

    def remove_customer_at(self, index):
        try:
            del self.customers[index]
            return f"Customer at index {index} removed"
        except IndexError:
            raise IndexError(f"No customer exists at index {index}")

    def get_customer_at(self, index):
        try:
            return self.customers[index]
        except IndexError:
            raise IndexError(f"No customer exists at index {index}")

    def get_num_customers(self):
        return len(self.customers) # + 1 (add to show testing of try except frontend.py)


def test_coffee_shop():
    shop = CoffeeShop()
    shop.add_customer("Alice")
    shop.add_customer("Bob")
    shop.add_customer("Charlie")
    print(f"There are {shop.get_num_customers()} customers")
    print(f"The customer at index 1 is {shop.get_customer_at(1)}")

    print(shop.get_customer_at(5))
    print(shop.get_customer_at(2))
    print(shop.remove_customer_at(10))
    print(shop.remove_customer_at(1))


if __name__ == "__main__":
    test_coffee_shop()