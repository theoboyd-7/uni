from tkinter import Tk, Frame, Label, Button, Toplevel, Text
from backend import Recipe, RecipeBook

class RecipeBookApp:

    def __init__(self, recipe_book):
        self.recipe_book = recipe_book

        self.win = Tk()
        self.win.title("Recipe Book")

        self.main_frame = Frame(self.win)
        self.main_frame.grid(
            row=0,
            column=0
        )

    def run(self):
        self.create_widgets()
        self.win.mainloop()

    def create_widgets(self):
        count = self.recipe_book.get_num_recipes()
        for i in range(count):
            recipe = self.recipe_book.get_recipe_by_index(i)
            # - label for recipe name
            recipe_name_label = Label(
                self.main_frame,
                text=recipe.name
            )
            recipe_name_label.grid(
                row=i,
                column=0,
                padx=5,
                pady=5
            )
            # - label for recipe time
            recipe_time_label = Label(
                self.main_frame,
                text=f"{recipe.time} mins"
            )
            recipe_time_label.grid(
                row=i,
                column=1,
                padx=5,
                pady=5
            )
            # button to view recipe --> command opens view_recipe_win
            view_button = Button(
                self.main_frame,
                text="View Recipe",
                command=lambda index=i:self.view_recipe(index)
            )
            view_button.grid(
                row=i,
                column=2
            )

    def view_recipe(self, index):
        recipe = self.recipe_book.get_recipe_by_index(index)

        view_win = Toplevel(self.win)
        view_win.title(f"{recipe.name}")
        # - label for recipe name row 0
        recipe_name_label = Label(
            view_win,
            text=recipe.name,
            font=('',15)
        )
        recipe_name_label.grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )
        # - label for recipe time row 1
        recipe_time_label = Label(
            view_win,
            text=f"Cook time: {recipe.time} minutes",
            font=('',10)
        )
        recipe_time_label.grid(
            row=1,
            column=0,
            padx=5,
            pady=5
        )
        # - text for recipe steps row 2
        text_widget = Text(
            view_win, 
            height=10, 
            width=30
        )
        text_widget.grid(
            row=2,
            column=0,
            padx=5,
            pady=5
        )

        text_widget.insert('1.0', f"{recipe.steps}")
        text_widget.config(state="disabled")


def main():
    recipe = Recipe("Spaghetti Bolognese", 30, "Step 1: Brown the meat.\nStep 2: Add tomato sauce.\nStep 3: Cook the pasta.")
    recipe2 = Recipe("Cheese Pasta", 15, "Step 1: Cook pasta.\nStep 2: Sprinkle on cheese.")
    recipe_book = RecipeBook()

    recipe_book.add_recipe(recipe)
    recipe_book.add_recipe(recipe2)

    app = RecipeBookApp(recipe_book)
    app.run()


main()