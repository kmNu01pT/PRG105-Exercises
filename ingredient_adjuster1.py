"""Find a simple recipe online, provide a link to the recipe in the comments.
Display the ingredients with amounts and list the servings that will be made with the recipe.
Ask the user to enter how many servings they would like to make,
and display the required amount of ingredients they will need. Format to one decimal place. """

# ingredients for macaroni and cheese
# based on 4 servings
box_elbow_macaroni_ounces = 8 / 4
butter_cup = 0.25 / 4
all_purpose_flour_cup = 0.25 / 4
salt_teaspoon = 0.5 / 4
milk_cups = 2 / 4
shredded_cheddar_cheese_cups = 2 / 4

print("This recipe will convert the macaroni and cheese recipe based on how many servings you want to make")
quantity = int(input("How many servings would you like to make?"))
print("For " + str(quantity) + " servings, you will need: ")

print("Elbow Macaroni: " + format(quantity * box_elbow_macaroni_ounces, ",.1f") + " ounces")
print("Butter: " + format(quantity * butter_cup, ",.1f") + " cups")
print("Flour: " + format(quantity * all_purpose_flour_cup, ",.1f") + " cups")
print("Salt: " + format(quantity * salt_teaspoon, ",.1f") + " teaspoons")
print("Milk: " + format(quantity * milk_cups, ",.1f") + " cups")
print("Shredded Cheddar Cheese: " + format(quantity * shredded_cheddar_cheese_cups, ",.1f") + " cups")


# https://www.allrecipes.com/recipe/238691/simple-macaroni-and-cheese/
