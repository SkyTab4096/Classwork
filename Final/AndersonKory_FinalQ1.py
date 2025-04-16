#!/usr/bin/env python3

TAX = 0.06 # Sets a global tax rate to use later in the program

def sales_tax(total): # Defines a function to calculate the sales tax
    sales_tax = total * TAX # Calculate the tax amount to be added to the transaction
    totalWithTax = total + sales_tax # Adds the sales tax to the total for the transaction
    return totalWithTax # Returns the total with included sales tax to the original function

def getTotal(message): # Defines a function to get the total from the user with error handling
    while True: # Starts a loop to run until the user enters a valid number
        try: # Attempts to run the following code
            total = float(input(message)) # Attempts to get a value from the user and turn it into a float
            return total # Return the entered total to the original function
        except ValueError: # If there was an error while turning the entered value into a number,
            print(f"Value entered not a valid number") # Display this error message

def main(): # Defines the main function of the program
    print(f"Sales Tax Calculator\n") # Display the title of the program
    total = getTotal("Enter total:\t\t") # Get and store the transaction total from the user
    totalAfterTax = round(sales_tax(total), 2) # Calculate and store the total after including sales tax
    print(f"Total After Tax:\t{totalAfterTax}") # Display the total with tax
    
if __name__ == "__main__": # If running the program standalone, run the following
    main() # Call the main function of the program
