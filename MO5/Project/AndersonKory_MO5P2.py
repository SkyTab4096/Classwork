#Name: Kory Anderson
#Class: INFO 1200
#Section: 001
#Professor: Sharp
#Date: 
#Assignment #: 5
#By submitting this assignment, I declare that the source code contained in this assignment was written #solely by me, unless specifically provided in the assignment. I attest that no part of this assignment, #in whole or in part, was directly created by Generative AI, unless explicitly stated in the assignment #instructions, nor obtained from a subscription service. I understand that copying any source code, #in whole or in part, unless specifically provided in the assignment, constitutes cheating, and that #I will receive a zero on this project if I am found in violation of this policy.

import KAconverter as c # Use the custom written program

def fm_Welcome(): # Define function to call to display a welcome message
    print("Kory Anderson's Feet / Meters Converter") # Welcome message
    print() # Print a blank line

def fm_Menu(): # Define a function to call to display a conversion menu
    print("Conversions Menu:") # Display the title of the menu
    print("a. Feet to Meters") # Option 1
    print("b. Meters to Feet") # Option 2

def main(): # The main part of the program
    fm_Welcome() # Display the welcome message
    while True: # While the user wants to continue run the following
        fm_Menu() # Display the menu
        choice = input("Select a conversion (a/b): ") # Get the menu choice from the user
        print() # Print a blank line
        if choice == "a": # If the user selects the first option run the following
            feet = float(input("Enter feet: ")) # Get a number of feet to convert from the user
            meters = c.toMeters(feet) # Calculate the number of meters from the feet
            print(f"{round(meters, 2)} meters") # Display the calculated meters
        elif choice == "b": # If the user selects the second option run the following
            meters = float(input("Enter meters: ")) # Get a number of meters from the user
            feet = c.toFeet(meters) # Calculate the number of feet from the given meters
            print(f"{round(feet, 2)} feet") # Display the feet calculated
        else: # Validation of the user's choice
            print("You did not enter a valid selection") # Display an invalid choice message
        more = input("Would you like to perform another conversion? (y/n): ") # Prompt the user to continue
        print() # Print a blank line
        if more != "y": # If the user selects anything other than 'y' run the following
            print("Thanks, bye!") # Exit message
            break # Stop the code

if __name__ == "__main__": main() # Run the progam if called directly