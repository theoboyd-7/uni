from tkinter import Tk, Frame, Label, Entry, Button, StringVar, Toplevel
from backend import TaskList

class TodoApp:

    def __init__(self, tasklist):
        self.tasklist = tasklist

        self.win = Tk()
        self.win.title("Todo")

        self.main_frame = Frame(self.win)
        self.main_frame.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
        )

        self.new_task = StringVar()
        self.task_widgets = []

    def run(self):
        self.create_widgets()
        self.win.mainloop()

    def create_widgets(self):
        self.delete_all_task_widgets()

        count = self.tasklist.get_num_tasks()
        for i in range(count):
            task = self.tasklist.get_task_message_by_index(i)
            task_label = Label(
                self.main_frame,
                text=task
            )
            task_label.grid(
                row=i+1,
                column=0,
                padx=5,
                pady=5,
            )
            self.task_widgets.append(task_label)

            edit_task_button = Button(
                self.main_frame,
                text="Edit",
                command=lambda index=i: self.edit_task(index, task=task)
            )
            edit_task_button.grid(
                row=i+1,
                column=1,
                padx=5,
                pady=5,
            )
            self.task_widgets.append(edit_task_button)

            remove_task_button = Button(
                self.main_frame,
                text="Remove",
                command=lambda index=i: self.remove_task(index)
            )
            remove_task_button.grid(
                row=i+1,
                column=2,
                padx=5,
                pady=5,
            )
            self.task_widgets.append(remove_task_button)

        task_entry = Entry(
            self.main_frame,
            textvariable=self.new_task
        )
        task_entry.grid(
            row=count+1,
            column=0,
            padx=5,
            pady=5,
        )

        add_task_button = Button(
            self.main_frame,
            text="Add",
            command=self.add_task
        )
        add_task_button.grid(
            row=count+1,
            column=1,
            padx=5,
            pady=5,
        )

    def add_task(self):
        task = self.new_task.get()
        self.tasklist.create_new_task(task)
        self.create_widgets()
        self.new_task.set("")

    def remove_task(self, index):
        self.tasklist.remove_task_at_index(index)
        self.create_widgets()

    def edit_task(self, index, task):
        new_win = Toplevel(self.win)
        new_win.title("Edit Task")

        edit_task_entry = Entry(
            new_win, 
            textvariable=task
        )
        edit_task_entry.grid(
            row=0,
            column=0
        )

        edit_task_button = Button(
            new_win, 
            text="Confirm",
            command=lambda :[
                self.tasklist.set_task_message_at_index(index, edit_task_entry.get()),
                self.create_widgets(),
                new_win.destroy()
            ]
        )
        edit_task_button.grid(
            row=0,
            column=1
        )

    def delete_all_task_widgets(self):
        for widget in self.task_widgets:
            widget.destroy()
        self.task_widgets = []


def main():
    tasklist = TaskList()

    tasklist.create_new_task("Buy Milk")
    tasklist.create_new_task("Buy Eggs")
    tasklist.create_new_task("Go to work")
    tasklist.create_new_task("Do the coursework")

    app = TodoApp(tasklist)
    app.run()


main()