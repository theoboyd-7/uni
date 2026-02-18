class Recipe:
    
    def __init__(self, name, time, steps):
        self.name = name
        self.time = time
        self.steps = steps

    def __str__(self):
        return f"Recipe for: {self.name} takes {self.time} mins and the steps are:\n {self.steps}"


class RecipeBook:

    def __init__(self):
        self.recipe_book = []

    def add_recipe(self, recipe):
        self.recipe_book.append(recipe)

    def remove_recipe_by_index(self, index):
        del self.recipe_book[index]

    def get_recipe_by_index(self, index):
        return self.recipe_book[index]
    
    def get_num_recipes(self):
        return len(self.recipe_book)
    
    def __str__(self):
        return f"{self.recipe_book}"


def test_recipe():
    recipe = Recipe("Spaghetti Bolognese", 30, "Step 1: Brown the meat. \n Step 2: Add tomato sauce. \n Step 3: Cook the pasta.")
    recipe2 = Recipe("Cheese Pasta", 15, "Step 1: Cook pasta. \n Step 2: Sprinkle on cheese.")
    print(recipe)
    print(recipe2)


    recipe_book = RecipeBook()

    print(recipe_book)

    recipe_book.add_recipe(recipe)
    recipe_book.add_recipe(recipe2)

    print(recipe_book)


# test_recipe()