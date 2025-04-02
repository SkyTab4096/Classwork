#Name: Kory Anderson
#Class: INFO 1200
#Section: 001
#Professor: Dr. Jason Sharp
#Date: April 9, 2025
#Assignment #: 8
#By submitting this assignment, I declare that the source code contained in this assignment was written #solely by me, unless specifically provided in the assignment. I attest that no part of this assignment, #in whole or in part, was directly created by Generative AI, unless explicitly stated in the assignment #instructions, nor obtained from a subscription service. I understand that copying any source code, #in whole or in part, unless specifically provided in the assignment, constitutes cheating, and that #I will receive a zero on this project if I am found in violation of this policy.

def displayTitle(): # Defines a function to display the title
    print(f"Kory Anderson's Wizard Inventory Game\n") # Print the title of the program

def printMenu(): # Defines a function to display the menu
    print(f"COMMAND MENU\n") # Title of the menu
    print(f"show - Show all items") # Command one
    print(f"grab - Grab an item") # Command two
    print(f"edit - Edit an item") # Command three
    print(f"drop - Drop an item") # Command four
    print(f"exit - Exit the program\n") # Command five

def show(inventory): # Defines the first command
    for number, item in enumerate(inventory, start = 1): # Makes a loop for every item in the inventory
        print(f"{number}. {item}\n") # Displays the item

def grabItem(inventory): # Defines a function to add a new item to the inventory
    if len(inventory) >= 4: # Checks to see if the inventory is larger than the allowed size
        print(f"You can't carry any more items.  Drop something first.\n") # Display an error message that the inventory is full
    else: # If there is space in the inventory, run the following
        item = input("Name:\t") # Get the new item from the player
        inventory.append(item) # Adds the new item to inventory
        print(f"{item} was added.\n") # Display that the item was added

def editItem(inventory): # Defines a function to edit an item in the inventory
    number = int(input("Number:\t")) # Gets a selector from the player for what item to edit
    if number < 1 or number > len(inventory): # Checks to see if the entered selector is smaller than 1 or greater than the number of items in the inventory
        print(f"Invalid number.  Please try again.") # Displays an error message that the selector is invalid
    else: # If the selector is valid,
        item = input("Updated name:\t") # Asks the player what to change the name of the item to
        inventory[number-1] = item # Redefine the item in the inventory to the updated name
        print(f"Item number {number} was updated.\n") # Display a message to the player that item was updated

def dropItem(inventory): # Defines a function to remove an item from the inventory
    number = int(input("Number:\t")) # Gets a selector from the player for what item to remove
    if number < 1 or number > len(inventory): # Checks to see if the entered selector is smaller than 1 or greater than the number of items in the inventory
        print(f"Invalid Number.  Please try again.\n") # Prints an error message to the player that the selector is invalid
    else: # If the selector is valid, run the following
        item = inventory.pop(number - 1) # Removes the item from the inventory
        print(f"{item} was dropped.\n") # Display a message to the player that the item was removed

def main(): # Defines a function for the main functionality of the program
    displayTitle() # Calls the function to display the title
    printMenu() # Calls the function to print the menu

    inventory = ["staff", "spellbook", "cloak"] # Sets a standard inventory

    while True: # Defines a loop for the commands
        command = input("Command:\t") # Gets the command from the user
        if command.lower() == "show": # Checks to see if the entered command is the first command
            show(inventory) # Calls the function for the first command
        elif command.lower() == "grab": # Checks to see if the entered command is the second command
            grabItem(inventory) # Calls the function for the second command
        elif command.lower() == "edit": # Checks to see if the entered command is the third command
            editItem(inventory) # Calls the function for the third command
        elif command.lower() == "drop": # Checks to see if the entered command is the fourth command
            dropItem(inventory) # Calls the function for the fourth command
        elif command.lower() == "exit": # Checks to see if the entered command is the fifth command
            break # Breaks the loop
        else: # If no valid command was entered, run the following
            print(f"Not a valid command. Please try again.\n") # Prints an error message to the player
        printMenu() # Reprints the command menu
    print(f"Bye!") # Prints an exit message to the player

if __name__ == "__main__": # If running the application standalone,
    main() # Run the main function of the program