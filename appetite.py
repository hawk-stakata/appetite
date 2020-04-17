guest_name = input("\nHi, welcome to Appetite. Can I have your name please? ")
party_size = int(input(f"\nThanks {guest_name}, and how many in your party? "))
menu = {
    "drinks": ["Water", "Coffee", "Tea", "Mimosa", "Bloody Mary", "Juice", "Soda"],
    "appetizers": ["Tots", "Chips n Salsa", "Cheese Plate", "Buffalo Wings", "Poke Nachos"],
    "mains": ["Breakfast Burrito", "Breakfast Sandwich", "French Toast", "Eggs Benedict", "Waffles"],
    "desserts": ["Cake", "Ice Cream", "Creme-brulee", "Brownies"]
}
drink_order = []
appetizer_order = []
food_order = []
dessert_order = []
order = {}

def greet_guests():
    global guest_name
    global party_size
    if party_size > 10:
        print("\nSorry, we can only seat parties of 10 or less. " + str(party_size - 10) + " of your friends have been banished from the brunch squad")
        party_size = 10
        print(f"{guest_name} and {guest_name}'s remaining friends, please follow me\n")
    else:
        print(f"Ok great! {guest_name} and {guest_name}'s entourage please follow me\n")

# def show_drink_menu():
#     print("Here's our drink menu:")
#     # Print drink menu
#     for x in menu["drinks"]:
#         print(x)
#
# def show_appetizers():
#     for x in menu["appetizers"]:
#         print(x)
#
# def show_mains():
#     for x in menu["mains"]:
#         print(x)

def show_menu(type):
    print(f"Here's our {type} menu")
    for item in menu[type]:
        print(item)


def validate_drink_order():
    global guest_drink
    if guest_drink in menu["drinks"]:
        print("Ok got it")
    else:
        while guest_drink not in menu["drinks"]:
            guest_drink = input("Sorry, we don't have that. Can I get you something else? ")

def validate_order(type):
    global guest_input
    if guest_input in menu[type]:
        print("Ok got it")
    else:
        while guest_input not in menu[type]:
            guest_input = input("Sorry, we don't have that. Can I get you something else? ")

def take_drink_order():
# def take_drink_order():
    # Declare global variables
    global drink_order
    global menu
    global guest_drink
    global guest_input
    # Ask if guests want drinks
    want_drinks = input("Can I start you off with some drinks? (yes/no): ")
    if want_drinks == "yes":
        # Print drink menu
        show_menu("drinks")
        # Take drink order
        # guest_drink = input("\nWhat would you like? ")
        guest_input = input("\nWhat would you like? ")
        # Validate drink order
        # validate_drink_order()
        validate_order("drinks")
        # Append drink to drink order
        # drink_order.append(guest_drink)
        drink_order.append(guest_input)
        # Ask for any other drinks
        # guest_drink = input("Anything else? ")
        guest_input = input("Anything else? ")
        # Loop through appending drinks until guests are done ordering
        # while guest_drink != "no":
        #     validate_drink_order()
        #     drink_order.append(guest_drink)
        #     guest_drink = input("Anything else? ")

        while guest_input != "no":
            validate_order("drinks")
            drink_order.append(guest_input)
            guest_input = input("Anything else? ")
        # Print drink order
        print("Ok that's: ")
        for x in drink_order:
            print(x)
        print("I'll be right back with those drinks")
        for num in range(0,3):
            print("...")
    else:
        print("Ok nothing to drink")

def bring_order(type):
    print("Ok here's your order: \n")
    if type == "drinks":
        for x in drink_order:
            print(x)
    elif type == "appetizers":
        for x in appetizer_order:
            print(x)
    elif type == "mains":
        for x in main_order:
            print(x)
    elif type == "desserts":
        for x in dessert_order:
            print(x)



greet_guests()
take_drink_order()
if len(drink_order) >= 1:
    bring_order("drinks")












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
