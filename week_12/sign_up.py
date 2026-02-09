from tkinter import Tk, Frame, Label, Entry, Button, Checkbutton, StringVar, BooleanVar
import re
import csv

class SignUp:

    def __init__(self):
        self.win = Tk()
        self.win.title("SignUp Page")
        self.win.geometry("400x200")

        self.main_frame = Frame(self.win)
        self.main_frame.grid(column=0, row=0, padx=10, pady=10)

        self.username = StringVar()
        self.password = StringVar()
        self.confirm_password = StringVar()
        self.message = StringVar()
        self.message.set("Enter username and password.")

    def run(self):
        self.create_widgets()
        self.win.mainloop()

    def create_widgets(self):
        self.label_message = Label(
            self.main_frame,
            textvariable=self.message,
            width=30
        )
        self.label_message.grid(column=0, row=0, columnspan=2)

        label_username = Label(
            self.main_frame,
            text="Username:"
        )
        label_username.grid(column=0, row=1)

        entry_username = Entry(
            self.main_frame,
            width=25,
            textvariable=self.username
        )
        entry_username.grid(column=1, row=1)

        label_password = Label(
            self.main_frame,
            text="Password:"
        )
        label_password.grid(column=0, row=2)

        self.entry_password = Entry(
            self.main_frame,
            width=25,
            textvariable=self.password,
            show="*"
        )
        self.entry_password.grid(column=1, row=2)

        label_confirm_password = Label(
            self.main_frame,
            text="Confirm Password:"
        )
        label_confirm_password.grid(column=0, row=3)

        self.entry_confirm_password = Entry(
            self.main_frame,
            width=25,
            textvariable=self.confirm_password,
            show="*"
        )
        self.entry_confirm_password.grid(column=1, row=3)

        self.check_var = BooleanVar()

        self.show = Checkbutton(
            self.main_frame, 
            text="Show Password", 
            variable=self.check_var, 
            command=self.show_pass
        )
        self.show.grid(column=0, row=4)

        button_sign_in = Button(
            self.main_frame,
            text="Sign In",
            command=self.sign_up
        )
        button_sign_in.grid(column=0, row=5)

        button_cancel = Button(
            self.main_frame,
            text="Cancel",
            command=self.win.destroy
        )
        button_cancel.grid(column=1, row=5)

    def sign_up(self):
        username = self.username.get()
        password = self.password.get()
        confirm_password = self.confirm_password.get()

        username_taken = False

        with open("week_12/users.csv", "r", newline="") as file:
            file = csv.reader(file)
            for row in file:
                if row[0] == username:
                    username_taken = True

        if len(password) >= 5:
            if re.search(r'\d', password) and re.search(r'[a-zA-Z]', password):
                if not username_taken:
                    if password == confirm_password:
                        self.message.set("Signed Up")
                        self.label_message.configure(fg="green")
                        with open("week_12/users.csv", "a", newline="") as file:
                            file = csv.writer(file)
                            file.writerow([username, password])
                    else:
                        self.message.set("Passwords do not match!")
                        self.label_message.configure(fg="red")
                else:
                    self.message.set("Username already exists!")
                    self.label_message.configure(fg="red")
            else:
                self.message.set("Password must contain a letter/number")
                self.label_message.configure(fg="red")
        else:
            self.message.set("Password must be at least 5 characters long")
            self.label_message.configure(fg="red")

    def show_pass(self):
        if self.check_var.get():
            self.entry_password.configure(show="")
            self.entry_confirm_password.configure(show="")
        else:
            self.entry_password.configure(show="*")
            self.entry_confirm_password.configure(show="*")
            

def main():
    app = SignUp()
    app.run()


main()