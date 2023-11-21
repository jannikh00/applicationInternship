"""
This program was an assignment I was given in university. Only the initial data was given.
We then received the following tasks for these. The program should be used to manage recipe data. 
In addition to the required functions/tasks, I also created an auxiliary function for printing all recipes.
"""

# Initial Data
recipeNames = ["Spaghetti Bolognese", "Chicken Tikka Masala", "Beef Tacos"]
spaghettiIngredients = ["spaghetti", "minced beef", "tomato sauce", "onion", "garlic"]
chickenTikkaIngredients = ["chicken breast", "yogurt", "tikka masala spice", "rice"]
beefTacosIngredients = ["ground beef", "taco shells", "lettuce", "tomato", "cheese"]

# Auxiliary function for clear printing of the recipes list
def print_recipes():
    for i in recipes:
        print(i)


# Task 1:
# Write a function `create_recipe()` that takes recipe name and a list of ingredients as parameters, and returns a dictionary representing the recipe.
def create_recipe(recipe_name, **ingredients):
    return {"recipe name": recipe_name, "ingredients": ingredients}


# Task 2:
# Use `create_recipe()` to create a recipe object for each of your recipes, and store them in a list called `recipes`.
recipes = [create_recipe("Spaghetti Bolognese", ing_1="spaghetti", ing_2="minced beef", ing_3="tomato sauce", ing_4="onion", ing_5="garlic"),
           create_recipe("Chicken Tikka Masala", ing_1="chicken breast", ing_2="yogurt", ing_3="tikka masala spice", ing_4="rice"),
           create_recipe("Beef Tacos",ing_1="ground beef", ing_2="taco shells", ing_3="lettuce", ing_4="tomato", ing_5="cheese")]

print("\nHere you can see a list of the currently available recipes:")
print_recipes()

# Task 3:
# Write a function `get_recipe()` that takes the recipe name as a parameter and returns the matching recipe object from the `recipes` list.
def get_recipe(requested_recipe):
    for i in recipes:
        if i["recipe name"] == requested_recipe:
            return i
    return ("The requested recipe isn't available.")
        

# Task 4:
# Use `get_recipe()` to retrieve the "Chicken Tikka Masala" recipe and print its details.
print("\nHere you can see a recipe for a >>Chicken Tikka Masala<<:")
print(get_recipe("Chicken Tikka Masala"))

# Task 5:
# Write a function `add_recipe()` that takes a recipe object as a parameter and adds it to the `recipes` list.
def add_recipe(new_recipe):
    recipes.append(new_recipe)


# Task 6:
# Use `add_recipe()` to add a new recipe to your `recipes` list.
Schnitzel = create_recipe("Schnitzel", ing_1="chicken", ing_2="breadcrumbs", ing_3="eggs", ing_4="potatoes")
add_recipe(Schnitzel)
print("\nHere is the recipe list after adding the recipe for a >>Schnitzel<<:")
print_recipes()

# Task 7:
# Write a function `remove_recipe()` that takes a recipe name as a parameter and removes the matching recipe object from the `recipes` list.
def remove_recipe(remove_recipe):
    for i in recipes:
        if i["recipe name"] == remove_recipe:
            recipes.remove(i)
    return ("The requested recipe isn't available.")


# Task 8:
# Use `remove_recipe()` to remove the "Beef Tacos" recipe from your `recipes` list.
remove_recipe("Beef Tacos")
print("\nHere's the recipe list after removing the >>Beef Tacos<<:")
print_recipes()

# Task 9:
# Write a function update_recipe() that takes a recipe name and a new ingredients list as parameters, and updates the matching recipe object in the recipes list.
def update_recipe(update_dict):
    for i in recipes:
        if i["recipe name"] == update_dict["recipe name"]:
            i["ingredients"] = update_dict["ingredients"]
            break
    return ("The requested recipe isn't available.")

# Task 10:
# Use `update_recipe()` to update the ingredients for your "Spaghetti Bolognese" recipe.
spaghettiNew = create_recipe("Spaghetti Bolognese", ing_1="spaghetti", ing_2="minced beef", ing_3="tomato sauce", ing_4="carots")
update_recipe(spaghettiNew)
print("\nHere's the recipe list with the updated >>Spaghetti Bolognese<< recipe:")
print_recipes()
