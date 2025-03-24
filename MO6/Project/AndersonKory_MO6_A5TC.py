#!/usr/bin/env python3

tax = 0.06 # Sets a standard tax rate

def sales_tax(total): # Defines a function to calculate sales tax
    sales_tax = total * tax # Calculates sales tax
    return sales_tax # Gives the calculated value to the main function

def main(): # Defines the main function
    print("Sales Tax Calculator\n") # Prints an application title
    total = float(input("Enter total: ")) # Gathers the total from the user 
    total_after_tax = round(total + sales_tax(total), 2) # Calculates the total after tax and rounds to two decimal places
    print("Total after tax: ", total_after_tax) # Tells the user the calculated value
    
if __name__ == "__main__": # Used when running standalone
    main() # Calls the main function
