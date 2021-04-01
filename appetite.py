# Python program designed to educate non-devs about programming concepts by simulating a restaurant.
# Note - this is meant to be primarily educational and simple, not necessarily to be the best possible working version of the app

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
main_order = []
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


def show_menu(type):
    print(f"Here's our {type} menu")
    for item in menu[type]:
        print(item)

def validate_order(type):
    global guest_input
    if guest_input in menu[type]:
        print("Ok got it")
    else:
        while guest_input not in menu[type] and guest_input.lower() != "no":
            guest_input = input("Sorry, we don't have that. Can I get you something else? ")

def append_item(type):
    global append_to_order
    append_to_order = ""
    if type == "drinks":
        # add to type_order var
        append_to_order = drink_order
        # add to total order object
        order["drinks"] = drink_order
    elif type == "appetizers":
        append_to_order = appetizer_order
        order["appetizers"] = appetizer_order
    elif type == "mains":
        append_to_order = main_order
        order["mains"] = main_order
    elif type == "desserts":
        append_to_order = dessert_order
        order["desserts"] = dessert_order

def print_order(type):
    global order_to_print
    order_to_print = ""
    if type == "drinks":
        order_to_print = drink_order
    elif type == "appetizers":
        order_to_print = appetizer_order
    elif type == "mains":
        order_to_print = main_order
    elif type == "desserts":
        order_to_print = dessert_order
    print("\n\nOk that's: ")
    for items in order_to_print:
        print(items)


def take_order(type):
    # Declare global variables
    global menu
    global guest_input
    global append_to_order
    # Ask if guests want to order
    want_to_order = input(f"Can I get you some {type}? (yes/no): ")
    if want_to_order == "yes":
        show_menu(type)
        # Take order
        guest_input = input("\nWhat would you like? ")
        while guest_input.lower() != "no":
            validate_order(type)
            if guest_input.lower() != "no":
                append_item(type)
                append_to_order.append(guest_input)
                guest_input = input("\nAnything else? ")
        # Print order
        print_order(type)
    else:
        print(f"Ok no {type} \n")

def bring_order(type):
    print("One moment please")
    for num in range(0,5):
        print("...")
    print("Ok here's your order:")
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
    print("\n")

greet_guests()

take_order("drinks")
if len(drink_order) >= 1:
    bring_order("drinks")

take_order("appetizers")
if len(appetizer_order) >= 1:
    bring_order("appetizers")

take_order("mains")
if len(main_order) >= 1:
    bring_order("mains")

take_order("desserts")
if len(dessert_order) >= 1:
    bring_order("desserts")

print("It's been a pleasure serving you today, I hope you enjoyed your meal. Let's close out.\nYou had: ")
if len(drink_order) >= 1:
    print("Drinks: " + str(drink_order))
if len(appetizer_order) >= 1:
    print("Apps: " + str(appetizer_order))
if len(main_order) >= 1:
    print("Mains: " + str(main_order))
if len(dessert_order) >= 1:
    print("Desserts: " + str(dessert_order))
print("\nYour total for this hip bougie SF brunch would normally be $1000, \nbut lucky for you the owner says this one is on the house. \nSee you next time!")
