#Name: Kory Anderson
#Class: INFO 1200
#Section: 001
#Professor: Dr. Jason Sharp
#Date: April 16, 2025
#Assignment #: 9
#By submitting this assignment, I declare that the source code contained in this assignment was written #solely by me, unless specifically provided in the assignment. I attest that no part of this assignment, #in whole or in part, was directly created by Generative AI, unless explicitly stated in the assignment #instructions, nor obtained from a subscription service. I understand that copying any source code, #in whole or in part, unless specifically provided in the assignment, constitutes cheating, and that #I will receive a zero on this project if I am found in violation of this policy.

import csv # Import the csv library to read and write csv files

def displayTitle(): # Defines a function to display the title of the program
    print(f"Kory Anderson's Monthly Sales\n") # Display the title

def displayMenu(): # Defines a command to display the command menu
    print(f"COMMAND MENU\n") # Title of the menu
    print(f"monthly\t- View monthly sales") # Command 1
    print(f"yearly\t- View yearly summary") # Command 2
    print(f"edit\t- Edit sales for a month") # Command 3
    print(f"exit\t- Exit the program") # Command 4

def readSales(filename='monthly_sales.csv'): # Defines a function to read and store the data in a csv file to a variable
    sales = [] # Creates an empty array
    with open(filename, 'r', newline="") as file: # Opens the file in readmode
        reader = csv.reader(file) # Defines the reader to read the csv file
        for row in reader: # For every row in the csv file
            sales.append(row) # Add the data to a new row in the sales array
    return sales # Return the sales array to the original function

def viewMonthlySales(sales): # Defines the function called for the first command
    for row in sales: # For every row in the sales array that is passed through,
        print(f"{row[0]} - {row[1]}") # Print the month and the sales for that month
    print() # Print a spacing line

def viewYearlySummary(sales): # Defines the function called by the second command
    total = 0 # Reset the total of the all the months
    for row in sales: # For every month stored in the sales variable
        amount = int(row[1]) # Stores the value of every month's sales numbers as an integer
        total += amount # Adds the value for the month to the total
    
    count = len(sales) # Gets the total number of months stored in the file

    average = total / count # Calculates the average sales for every month
    average = round(average, 2) # Rounds the average to two decimal points

    print(f"Yearly total:\t\t{total}") # Displays the yearly total to the user
    print(f"Monthly average:\t{average}\n") # Displays the average for the months to the user

def edit(sales, filename): # Defines a function to be called by the third command
    names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] # Sets up a list all valid three-letter month abriviations
    name = input("Month:\t\t") # Gets what month the user wants to edit
    name = name.title() # Makes sure the first letter of the value the user enters is capitalized
    if name in names: # Checks to see if what the user entered is in the list of valid abrivations
        index = names.index(name) # Gets which month the user entered from the order of the valid list
        amount = int(input("Sales Amount:\t")) # Gets the new value from the user to store
        month = [] # Creates a new array to store what the user entered
        month.append(name) # Sets the first value in the new month array to be the name of the month
        month.append(str(amount)) # Sets the second value to be the amount the user entered
        sales[index] = month # Sets the proper row in the sales variable to the new values entered
        writeSales(sales, filename) # Writes the sales variable to the monthly_sales.csv file
        print(f"Sales amount for {month[0]} was modified.\n") # Let the user know that the data was actually modified
    else: # If the user did not enter a valid month,
        print(f"Invalid three-letter month") # Print an error message to the user

def writeSales(sales, filename): # Defines a function to write the csv file
    with open(filename, 'w', newline="") as file: # Opens the file in write mode
        writer = csv.writer(file) # Creates the writer to write the data
        writer.writerows(sales) # Write the data

def main(): # Defines the primary function of the program
    displayTitle() # Display the title
    displayMenu() # Display the command menu

    sales = readSales() # Stores the values of the csv file in the sales variable

    while True: # Create a loop to keep running the program
        command = input("Command: ") # Get the command the user wants to run
        print() # Print a spacing line
        if command == "monthly": # Checks to see if the command entered is the first command
            viewMonthlySales(sales) # Call the function to display the contents of the csv file
            displayMenu() # Redisplay the command menu
        elif command == "yearly": # Checks to see if the command entered is the second command
            viewYearlySummary(sales) # Call the function to display the yearly total and monthly average from the csv file
            displayMenu() # Redisplay the command menu
        elif command == "edit": # Checks to see if the command entered is the third command
            edit(sales, 'monthly_sales.csv') # Calls the function to edit the contents of the csv file
            displayMenu() # Redisplays the command meny
        elif command == "exit": # Checks to see if the command entered is the final command
            break # Stop the loop
        else: # If no valid command was entered, run the following
            print(f"Not a valid command. Please try again.\n") # Display an error message
            displayMenu() # Redisplay the command menu
    
    print("Bye!") # Print an exit message

if __name__ == "__main__": # If running the file standalone, run the following
    main() # Calls the main function of the program