#Name: Kory Anderson
#Class: INFO 1200
#Section: 001
#Professor: Dr. Jason Sharp
#Date: April 22, 2025
#Assignment #: Insert assignment number
#By submitting this assignment, I declare that the source code contained in this assignment was written #solely by me, unless specifically provided in the assignment. I attest that no part of this assignment, #in whole or in part, was directly created by Generative AI, unless explicitly stated in the assignment #instructions, nor obtained from a subscription service. I understand that copying any source code, #in whole or in part, unless specifically provided in the assignment, constitutes cheating, and that #I will receive a zero on this project if I am found in violation of this policy.

import csv # Import the csv library to read and write csv files

FILENAME = "contacts.csv" # Sets the name of the file that stores the contacts

def displayTitle(): # Defines a function to display the title of the program
    print(f"Kory Anderson's Contact Manager App\n") # Display the title

def displayMenu(): # Defines a function to display the command menu
    print(f"COMMAND MENU\n") # Title of the menu
    print(f"list - Display all contacts") # Command 1
    print(f"view - View a contact") # Command 2
    print(f"add - Add a contact") # Command 3
    print(f"del - Delete a contact") # Command 4
    print(f"exit - Exit program\n") # Exit command

def main(): # main function of the program
    contacts = readContacts() # Get and store the contents of the contacts.csv file
    displayTitle() # Display the title of the program 
    displayMenu() # Display the command menu
    while True: # Create a loop to run until the user exits
        command = input("Command:\t") # Get a command from the user 
        if command.lower() == "list": # Checks to see if the command entered is the first valid command
            listContacts(contacts) # Calls the function to display all contacts
        elif command.lower() == "view": # Checks to see if the command entered is the second valid command
            viewContact(contacts) # Calls the function to display the details of a single contact
        elif command.lower() == "add": # Checks to see if the command entered is the third valid command
            addContact(contacts) # Calls the function to add a single contact to the list
        elif command.lower() == "del": #  Checks to see if the command entered is the fourth valid command
            delContact(contacts) # Calls the function to remove a single contact from the list
        elif command.lower() == "exit": # Checks to see if the command entered is the fifth and final valid command
            break # Stop the loop
        else: # If no valid command was entered
            print(f"{command} not a valid command.  Please try again.") # Display an error message
        displayMenu() # Display the command menu again

def listContacts(contacts): # Defines the function to display all contacts
    if len(contacts) == 0: # Checks to make sure that there is contacts stored
        print(f"Contact list is empty.  Please add contacts and try again.") # Display an error message if no contacts are present
    else: # If there is at least one contact present,
        for i, row in enumerate(contacts, start=1): # Define a loop to display every contact
            print(f"{i}. {row[0]}") # Display each contact
        print() # Print a spacing line

def viewContact(contacts): # Define the function the display the details of a contact
    number = getContactNumber(contacts) # Gets an index for the contact that the user wants to see
    if number > 0: # If the number that was returned is valid,
        contact = contacts[number - 1] # Store the array of information that is in the master array
        print(f"Name:\t{contact[0]}") # Display the contact's name
        print(f"Email:\t{contact[1]}") # Display the contact's email address
        print(f"Phone:\t{contact[2]}\n") # Display the contact's phone number

def getContactNumber(contacts): # Defines the function to get an index number from the user
    while True: # Start a loop until the user enters a valid number
        try: # Start a loop with built-in error handling
            number = int(input("Number:\t")) # Attempt to store the value the user enters for the contact index
        except ValueError: # If there specifically was an error while turning what the user entered into an integer,
            print("Invalid Integer.\n") # Display an error message
            return -1 # Return an invalid index number to original function
        
        if number < 1 or number > len(contacts): # If the user entered a value that is not a natural number or is larger than the total number of contacts
            print("Invalid contact number.") # Display an error message
            return -1 # Return an invalid index number to the original function
        else: # If the entered value was valid,
            return number # Return the value the user entered
        
def addContact(contacts): # Defines a function to add a contact
    name = input("Name:\t") # Get the name of the contact from the user
    email = input("Email:\t") # Get the email from the user 
    phone = input("Phone:\t")# Get the phone number from the user
    
    contact = [] # Create a new empty array
    contact.append(name) # Store the name in the array
    contact.append(email) # Store the email in the array
    contact.append(phone) # Store the phone number in the array
    contacts.append(contact) # Store the new array into the master contacts array
    writeContacts(contacts) # Store the contents of the master contacts array into a csv file

    print(f"{contact[0]} was added.\n") # Tell the user that the contact was successfully created

def writeContacts(contacts): # Define the function to create and overwrite the csv file
    with open(FILENAME, "w", newline="") as file: # Open the file
        writer = csv.writer(file) # Create the writer
        writer.writerows(contacts) # Write the contents of the master contacts array to the csv file

def delContact(contacts): # Define a function to remove a contact
    number = getContactNumber(contacts) # Get an contact index from the user
    if number > 0: # If a valid index number was given,
        contact = contacts.pop(number - 1) # Store the contact and remove it from the master contact array
        print(f"{contact[0]} was deleted.\n") # Inform the user that the contact was successfully removed
    writeContacts(contacts) # Overwrite the contacts csv file

def readContacts(): # Defines a function to read the contents of the csv file
    contacts = [] # Create an empty array
    try: # Create a loop with built-in error handling
        with open(FILENAME, "r", newline="") as file: # Attempt to open the csv file
            reader = csv.reader(file) # Create the reader
            for row in reader: # For every row that the reader finds in the file,
                contacts.append(row) # Add the row to the new contacts array
    except FileNotFoundError: # If the file does not exist
        print(f"Could not find contacts file! Starting new contacts file...") # Display an error message
    return contacts # Return the contacts array, either with the contents of the file, or empty

if __name__ == "__main__": # If running standalone
    main() # Run the main function of the program