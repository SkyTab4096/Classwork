#! /usr/bin/env python3

import csv # Import the csv library to read and write csv files

def displayMenu(): # Defines a function to display the command list
    print(f"COMMAND MENU\n") # Menu title
    print(f"add - Add Item") # Command one
    print(f"del - Delete Item") # Command two
    print(f"list - List All Items") # Command three
    print(f"detail - List All Details of an item")
    print(f"exit - Exit the Program\n") # Command four

def readInventory(fileName="inventory.csv"): # Defines a function to read the contents of the inventory file
    inventory = [] # Creates a new list to store the contents of the file
    try: # Attempts to read the file
        with open(fileName, "r", newline="") as file: # Opens the file for the contents to be read
            reader = csv.reader(file) # Reads and stores the contents of the csv file
            for row in reader: # For every row that was read in the file
                inventory.append(row) # Add the row to the inventory array
        return inventory # Return the inventory array to the orginal function
    except FileNotFoundError: # If there was an issue finding the file run the following block of code
        return inventory # Return the empty array to the original function

def writeInventory(inventory, fileName="inventory.csv"): # Defines a function to write the inventory csv file
    with open(fileName, "w", newline="") as file: # Opens the file to be written
        writer = csv.writer(file) # Creates the writer to write the contents of the inventory array
        writer.writerows(inventory) # Write the contents of the inventory array

def getNum(message): # Define a function to validate the contents of what the user enters
    while True: # Create a loop to run until the user enters a valid number
        try: # Attempt to run the following block of code
            number = float(input(message)) # Attempt to store the value the user enters as a number
            return number # Return the number to the original function
        except ValueError: # If there was an error while storing as a number,
            print("Invalid Number. Please try again.") # Display this error message

def getInt(message): # Define a function to validate that the user enters an integer
    while True: # Create a loop to run until the user enters a valid integer
        try: # Attempt to run the following block of code
            integer = int(input(message)) # Get and store the value the user enters as an integer
            return integer # Return the integer entered to the original function
        except ValueError: # If there was an error while storing as an integer
            print("Invalid Integer. Please try again.") # Display this error message

def findItem(inventory, value): # Check to see if the supplied value is in the inventory
    counter = -1 # Start a counter to be zero when running
    for row in inventory: # For every item in the inventory,
        counter += 1 # Add one to the counter
        if value in row: # Check to see if the supplied value is in the inventory
            return counter # Return the counter to the original function

def newItem(inventory): # Defines a function to add an item to the inventory
    item = [] # Create a new empty array for the item
    #itemIndex = getInt("Item Index Number:\t") # An old version of the item index
    itemIndex = len(inventory) # The new version of the item index
    itemCode = input("Item Look Up Code:\t") # Get a barcode from the user
    itemName = input("Item Name:\t\t") # Get the name of the item from the user
    itemCost = round(getNum("Item Cost:\t\t"), 3) # Get the cost of the item from the user
    itemPrice = getNum("Item Price:\t\t") # Get what the user is charging for the item from the user
    itemReorderNumber = input("Reorder Number:\t\t") # Get the sku number from the user for future ordering
    qtyOnHand = getInt("Qty On Hand:\t\t") # Get how many copies of this item are currently on hand
    item.append(itemIndex) # Add the index to the item
    item.append(itemCode) # Add the barcode to the item
    item.append(itemName) # Add the name to the item
    item.append(itemReorderNumber) # Add the sku number to the item
    item.append(itemCost) # Add the cost to the item
    item.append(itemPrice) # Add the price to the item
    item.append(qtyOnHand) # Add the quantity to the item
    inventory.append(item) # Add the item to the inventory
    writeInventory(inventory) # Write the current inventory to the csv file
    print(f"{item[1]} was added to the inventory") # Let the user know that the item was created successfuly

def removeItem(inventory): # Defines a function to remove an item from the inventory
    itemCode = input("Item Look Up Code:\t") # Get a barcode from the user
    while True: # Defines a loop to run until the item is removed
        try: # Attempt to run the following block of code
            row = findItem(inventory, itemCode) # Find the row that contains the entered barcode
            removedItem = inventory.pop(row) # Remove the item from the inventory array
            writeInventory(inventory) # Store the new inventory array with the removed item
            print(f"{removedItem[2]} was removed.") # Inform the user that the item was removed
            break # Stop the loop
        except TypeError: # If there was an error while removing the item,
            print(f"No item with item code '{itemCode}'") # Display this error message
            break # Stop the loop

def listInventory(inventory): # Defines a function to display every item in inventory
    if len(inventory) == 0: # Checks to make see if there are items in inventory
        print("No items in inventory.") # Display an error message
    else: # If there is items in the inventory
        for item in inventory: # For every item in inventory
            print(f"Index:\t{item[0]}") # Display the index for the item
            print(f"Name:\t{item[2]}") # Display the name of the item
            print(f"Qty:\t{item[6]}") # Display how many of that item are on hand
            print(f"Price:\t{item[5]}") # Display the price of the item
            print(f"Cost:\t{item[4]}\n") # Display the cost of the item

def displayItem(inventory): # Defines a function to display all details of an item
    itemCode = input("Item Look Up Code:\t") # Gets a barcode from the user
    while True: # Starts a loop until the item is displayed
        try: # Attempt to run the following block of code
            row = findItem(inventory, itemCode) # Gets the row that contains the entered barcode
            item = inventory[row] # Get the item from inventory
            print(f"Index:\t\t{item[0]}") # Displays the index number of the item
            print(f"Barcode:\t\t{item[1]}") # Displays the barcode of the item
            print(f"Name:\t\t{item[2]}") # Displays the name of the item
            print(f"Reorder Number:\t{item[3]}") # Displays the reorder number of the item
            print(f"Cost:\t\t{item[4]}") # Displays the cost of the item
            print(f"Price:\t\t{item[5]}") # Displays the price of the item
            print(f"Qty:\t\t{item[6]}") # Displays the currently on hand quantity of the item
            break # Stops the loop
        except Exception as e: # If there was an error while running the code
            print(type(e), e) # Display the error
            break # Stop the loop

def main(): # Defines the main function of the program
    inventory = readInventory() # Stores the inventory in an array
    print("Kory Anderson's Inventory Manager\n") # Display the title of the program
    while True: # Start a loop for the program
        displayMenu() # Display the command menu
        command = input("Command: ") # Get a command from the user
        print() # Print a spacing line
        if command.lower() == "add": # Checks to see if the command entered is the first command
            newItem(inventory) # Calls the function to add a new item into inventory
        elif command.lower() == "del": # Checks to see if the command entered is the second command
            removeItem(inventory) # Calls the function to delete an item
        elif command.lower() == "list": # Checks to see if the command entered is the third command
            listInventory(inventory) # Calls the function to display all inventory items
        elif command.lower() == "detail": # Checks to see if the command entered is the fourth command
            displayItem(inventory) # Calls the function to display all details of an item
        elif command.lower() == "exit": # Checks to see if the command entered is the fifth command
            break # Stop the loop of the loop of the main function
        else: # If no valid command is entered,
            print(f"{command} not a valid command. Please try again.") # Display an error message
    print("Bye") # Display an exit message

if __name__ == "__main__": # If running the program standalone,
    main() # Call the main function of the program