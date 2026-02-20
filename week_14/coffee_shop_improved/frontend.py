from tkinter import Tk, Frame, Entry, Button, Label, StringVar, messagebox
from backend import CoffeeShop


class CoffeeShopApp:

    def __init__(self, coffee_shop):
        self.coffee_shop = coffee_shop

        self.win = Tk()
        self.win.title("Coffee Shop")

        self.main_frame = Frame(self.win)
        self.main_frame.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
        )

        self.new_customer_name = StringVar()

        self.customer_widgets = []

    def run(self):
        self.create_widgets()
        self.win.mainloop()

    def create_widgets(self):
        self.delete_all_customer_widgets()

        customer_entry = Entry(
            self.main_frame,
            textvariable=self.new_customer_name
        )
        customer_entry.grid(
            row=0,
            column=0,
            padx=5,
            pady=5,
        )

        add_customer_button = Button(
            self.main_frame,
            text="Add",
            command=self.add_customer
        )
        add_customer_button.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
        )

        count = self.coffee_shop.get_num_customers()
        for i in range(count):
            try:
                customer = self.coffee_shop.get_customer_at(i)
            except IndexError as e:
                messagebox.showerror(f"Error:", str(e))
                continue
            
            customer_label = Label(
                self.main_frame,
                text=customer
            )
            customer_label.grid(
                row=i+1,
                column=0,
                padx=5,
                pady=5,
            )
            self.customer_widgets.append(customer_label)

            remove_customer_button = Button(
                self.main_frame,
                text="Remove",
                command=lambda index=i: self.remove_customer(index)
            )
            remove_customer_button.grid(
                row=i+1,
                column=1,
                padx=5,
                pady=5,
            )
            self.customer_widgets.append(remove_customer_button)

        test_error_button = Button(
            self.main_frame,
            text="Test Error (Index 99)",
            command=lambda: self.remove_customer(99)
        )
        test_error_button.grid(
            row=count+1,
            column=0,
            columnspan=2,
            pady=20
        )
        self.customer_widgets.append(test_error_button)

    def add_customer(self):
        name = self.new_customer_name.get()
        self.coffee_shop.add_customer(name)
        self.create_widgets()
        self.new_customer_name.set("")  # Clear the entry box

    def remove_customer(self, index):
        try:
            self.coffee_shop.remove_customer_at(index)
        except IndexError as e:
            messagebox.showerror(f"Error:", str(e))

        self.create_widgets()

    def delete_all_customer_widgets(self):
        for widget in self.customer_widgets:
            widget.destroy()
        self.customer_widgets = []


def main():
    coffee_shop = CoffeeShop()

    coffee_shop.add_customer("Tatenda")
    coffee_shop.add_customer("Fahad")
    coffee_shop.add_customer("Xinran")

    app = CoffeeShopApp(coffee_shop)
    app.run()


main()