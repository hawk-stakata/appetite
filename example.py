
# Variables can store single things like defining table numbers
table_1 = "This table right here"
table_2 = "That table over there"

# Our mimosa and omelette vars are arrays
mimosa = ["champagne", "orange juice"]
omelette = ["eggs", "bacon", "cheese"]

# Arrays can also look like this
bloody_mary = [
    "vodka",
    "tomato juice",
    "lemon",
    "salt",
    "pepper",
    "worcestershire",
    "tabasco"
]

# Arrays can hold different types of data
drinks = [mimosa, "water", "coffee", bloody_mary, "tea"]

# We can access items in an arry by their index: var[x]
spencer_drink_order = "Spencer wants a " + str(drinks[3])

# Objects can organize information with key value pairs
object = {
    "key": "value"
}
# Stored data is usually related in some way
spencer = {
    "age": 29,
    "email_address": "stakata@google.com",
    "opt_in": True,
}

# Objects can be nested inside other objects,
# and store different types of data
brunch_squad = {
    "number_of_guests": 5,
    "order": {
        "guest_1": {
            "drink_order": ["water", "bloody mary"],
            "food_order": "breakfast burrito",
            "is_hungover": True,
        },
        "guest_2": {
            "drink_order": "coffee",
            "food_order": "french toast",
            "is_hungover": False,
        }
        # So on and so forth....
    }
}


# Functions hold a set of instructions
def make_cheeseburger():
    print("Gather all ingredients")
    print("Slice tomato, mushroom, onion, cheese")
    print("Cook patty")
    print("Grill onions and mushrooms")
    print("Melt cheese on patty")
    print("Stack ingredients inside the bun")

# We have to call our function before steps are executed
make_cheeseburger()

# Functions can accept variable data, perform math, and much more
def greet_guests():
    name = input("What's your name? ")
    print(f"Hi {name}, welcome to Appetite. Would you like a table?")

greet_guests() #Hi Spencer, welcome to Appetite. Would you like a table?

# We use an array for items in each place setting
place_settings = ["plate", "cup", "fork", "knife", "spoon", "napkin"]
# Shorthand notation for making 15 tables
tables = range(0,15)
# For each table in our 15 tables, give each seat a place setting
for table in tables:
    print("Give each seat" + str(place_settings))


# We define a condition to be used in our loop
is_eating = True
# We declare a function to fill water, that can be called later
def refill_water():
    print("Would you like more water?")

# While loop will run as long as is_eating remains true
while is_eating == True:
    refill_water() # Would you like more water?
    print("Check again in 10 minutes")
    # Beware the infinite loop!
    # Without this, our while loop will run forever
    is_eating = False

# We can define a dessert_menu variable
dessert_menu = ["cake", "ice cream", "creme-brulee", "brownies"]
# And prompt the user to tell us if they want dessert or not
want_dessert = input("Would you like dessert (yes/no)? ")

# Conditional If/Else statements are used to execute different
# code blocks depending on certain conitions
if want_dessert == "yes":
    # We can use our dessert_menu variable inside the conditional
    print("Here is our dessert menu" + str(dessert_menu))
else:
    print("Ok I'll be right back with your check")

party_size = input("How many in your party? ")

# Conditionals can evaluate numerical conditions too
if party_size > 12:
    print("Sorry, we don't have any tables that big")
else:
    print("Ok, just a moment please")
