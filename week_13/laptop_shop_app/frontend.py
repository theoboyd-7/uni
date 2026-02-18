from tkinter import Tk, Frame, Label, Entry, Button, StringVar, IntVar, DoubleVar, Toplevel, OptionMenu
from backend import ShoppingCart, Laptop, GamingLaptop

class LaptopShoppingApp:

    def __init__(self, shopping_cart):
        self.shopping_cart = shopping_cart

        self.win = Tk()
        self.win.title("Shopping Cart App")

        self.main_frame = Frame(self.win)
        self.main_frame.grid(
            row=0,
            column=0,
            padx=10,
            pady=10
        )

        self.laptop_widgets = []
        self.update_widgets = []

        self.new_laptop_brand = StringVar()
        self.new_laptop_price = DoubleVar(value=0.0)
        self.new_laptop_ram = IntVar(value=4)
        self.new_laptop_gpu = StringVar()

        self.ram_selected_option = StringVar(value=4)
        self.gpu_selected_option = StringVar(value="NVIDIA GTX 1650")

    def run(self):
        self.create_widgets()
        self.win.mainloop()

    def create_widgets(self):
        self.delete_all_laptop_widgets()
        
        count = self.shopping_cart.get_num_laptops()
        for i in range(count):
            laptop = self.shopping_cart.get_laptop_by_index(i)
            laptop_label = Label(
                self.main_frame,
                text=laptop
            )
            laptop_label.grid(
                row=i+1,
                column=0,
                padx=5,
                pady=5
            )
            self.laptop_widgets.append(laptop_label)

            update_laptop_button = Button(
                self.main_frame,
                text="Update",
                command=lambda index=i: self.update_laptop(index)
            )
            update_laptop_button.grid(
                row=i+1,
                column=1,
                padx=5,
                pady=5,
            )
            self.laptop_widgets.append(update_laptop_button)

            remove_laptop_button = Button(
                self.main_frame,
                text="Remove",
                command=lambda index=i: self.remove_laptop(index)
            )
            remove_laptop_button.grid(
                row=i+1,
                column=2,
                padx=5,
                pady=5,
            )
            self.laptop_widgets.append(remove_laptop_button)

        laptop_brand_entry = Entry(
            self.main_frame,
            textvariable=self.new_laptop_brand
        )
        laptop_brand_entry.grid(
            row=count+1,
            column=0,
            padx=5,
            pady=5,
        )
        self.laptop_widgets.append(laptop_brand_entry)

        laptop_price_entry = Entry(
            self.main_frame,
            textvariable=self.new_laptop_price
        )
        laptop_price_entry.grid(
            row=count+1,
            column=1,
            padx=5,
            pady=5,
        )
        self.laptop_widgets.append(laptop_price_entry)

        laptop_ram_entry = Entry(
            self.main_frame,
            textvariable=self.new_laptop_ram
        )
        laptop_ram_entry.grid(
            row=count+1,
            column=2,
            padx=5,
            pady=5,
        )
        self.laptop_widgets.append(laptop_ram_entry)

        laptop_gpu_entry = Entry(
            self.main_frame,
            textvariable=self.new_laptop_gpu
        )
        laptop_gpu_entry.grid(
            row=count+1,
            column=3,
            padx=5,
            pady=5,
        )
        self.laptop_widgets.append(laptop_gpu_entry)

        add_laptop_button = Button(
            self.main_frame,
            text="Add",
            command=lambda: [
                self.add_laptop(
                    self.new_laptop_brand.get(), 
                    self.new_laptop_price.get(), 
                    self.new_laptop_ram.get(), 
                    self.new_laptop_gpu.get()
                ), 
                self.create_widgets()
            ]
        )
        add_laptop_button.grid(
            row=count+1,
            column=4,
            padx=5,
            pady=5,
        )
        self.laptop_widgets.append(add_laptop_button)

    def add_laptop(self, brand, price, ram=4, gpu=""):
        price = float(price)
        ram = int(ram)
        
        if len(gpu) == 0:
            new_laptop = Laptop(brand, price)
            new_laptop.ram = ram
            self.shopping_cart.add_laptop(new_laptop)
        elif len(gpu) > 0:
            new_gaming_laptop = GamingLaptop(brand, price)
            new_gaming_laptop.ram = ram
            new_gaming_laptop.gpu = gpu
            self.shopping_cart.add_laptop(new_gaming_laptop)
        
        self.new_laptop_brand.set("")
        self.new_laptop_price.set("")
        self.new_laptop_ram.set("")
        self.new_laptop_gpu.set("")
        self.create_widgets()

    def update_laptop(self, index):
        self.delete_all_update_widgets()
        laptop = self.shopping_cart.get_laptop_by_index(index)

        self.ram_selected_option.set(laptop.ram)

        update_win = Toplevel(self.win)
        update_win.title("Update Laptop")

        ram_label = Label(
            update_win,
            text="Update RAM of Laptop"
        )
        ram_label.grid(
            row=0,
            column=0
        )
        self.update_widgets.append(ram_label)

        ram_option_menu = OptionMenu(
            update_win,
            self.ram_selected_option,
            4,
            8,
            16,
            32
        )
        ram_option_menu.grid(
            row=0,
            column=1
        )
        self.update_widgets.append(ram_option_menu)

        if isinstance(laptop, GamingLaptop):
            self.gpu_selected_option.set(laptop.gpu)

            gpu_label = Label(
                update_win,
                text="Update GPU of Laptop"
            )
            gpu_label.grid(
                row=1,
                column=0
            )
            self.update_widgets.append(gpu_label)

            gpu_option_menu = OptionMenu(
                update_win,
                self.gpu_selected_option,
                "NVIDIA GTX 1650",
                "NVIDIA RTX 3070",
                "NVIDIA RTX 4080",
                "AMD RX 6800M"
            )
            gpu_option_menu.grid(
                row=1,
                column=1
            )
            self.update_widgets.append(gpu_option_menu)
        else:
            gpu_label = Label(
                update_win, 
                text="Graphics Not upgradeable"
            )
            gpu_label.grid(
                row=1,
                column=0
            )
            self.update_widgets.append(gpu_label)

        confirm_laptop_button = Button(
                update_win,
                text="Update",
                command=lambda: [
                    self.shopping_cart.update_laptop_at_index(
                        index, 
                        int(self.ram_selected_option.get()), 
                        self.gpu_selected_option.get()
                    ),
                    update_win.destroy(),
                    self.create_widgets()
                ]
            )
        confirm_laptop_button.grid(
            row=2,
            column=0,
            padx=5,
            pady=5,
        )
        self.update_widgets.append(confirm_laptop_button)
    
    def remove_laptop(self, index):
        self.shopping_cart.remove_laptop(index)
        self.create_widgets()

    def delete_all_laptop_widgets(self):
        for widget in self.laptop_widgets:
            widget.destroy()
        self.laptop_widgets = []

    def delete_all_update_widgets(self):
        for widget in self.update_widgets:
            widget.destroy()
        self.update_widgets = []


def main():
    shopping_cart = ShoppingCart()

    laptop = Laptop("HP", 259.99)
    laptop1 = Laptop("Asus", 1259.99)
    laptop2 = Laptop("Macbook", 1399.99)

    shopping_cart.add_laptop(laptop)
    shopping_cart.add_laptop(laptop1)
    shopping_cart.add_laptop(laptop2)

    gaming_laptop = GamingLaptop("ASUS", 2599.99)
    gaming_laptop.gpu = "NVIDIA RTX 4080"
    gaming_laptop.ram = 32

    shopping_cart.add_laptop(gaming_laptop)

    app = LaptopShoppingApp(shopping_cart)
    app.run()

main()