from tkinter import Tk, Frame, Label, Entry, Button, IntVar, StringVar
import math

class Circle:

    def __init__(self):
        self.win = Tk()
        self.win.title("Converter")
        self.win.geometry("200x150")

        self.main_frame = Frame(self.win)
        self.main_frame.pack(padx=10, pady=10)

        self.radius = IntVar()
        self.area = StringVar()
        self.area.set("Area: 0cm^2")
        self.circumference = StringVar()
        self.circumference.set("Circumference: 0cm")

    def run(self):
        self.create_widgets()
        self.win.mainloop()

    def create_widgets(self):
        label_radius = Label(
            self.main_frame,
            text="Radius:"
        )
        label_radius.pack()

        entry_num1 = Entry(
            self.main_frame,
            width=20,
            textvariable=self.radius
        )
        entry_num1.pack()

        label_area = Label(
            self.main_frame,
            textvariable=self.area
        )
        label_area.pack()

        label_circumference = Label(
            self.main_frame,
            textvariable=self.circumference
        )
        label_circumference.pack()

        button_calc = Button(
            self.main_frame,
            text="Calculate",
            command=self.calc
        )
        button_calc.pack(side="left")

        button_close = Button(
            self.main_frame,
            text="Close",
            command=self.win.destroy
        )
        button_close.pack(side="right")

    def calc(self):
        radius = self.radius.get()

        area = math.pi * (radius ** 2)
        circumfernce = math.pi * (2 * radius)

        self.area.set(f"Area: {area:.2f}cm^2")
        self.circumference.set(f"Circumference: {circumfernce:.2f}cm")


def main():
    circ = Circle()
    circ.run()


main()

