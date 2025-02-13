#!/usr/bin/env python3

# display a welcome message
print("Kory Anderson's Miles Per Gallon application") # Welcome message
print() # Print a blank line

another_trip = "y" # Set the default choice
while another_trip == "y": # Run the following code only if the user chooses to
    # get input from the user
    miles_driven = float(input("Enter miles driven:\t\t")) # Grab and store the miles driven
    gallons_used = float(input("Enter gallons of gas used:\t")) # Grab and store gallons used
    cost_per_gallon = float(input("Enter cost per gallon:\t\t")) # Grab and store cost per gallon

    if miles_driven <= 0: # Validate the miles driven
        print("Miles driven must be greater than zero. Please try again.") # Error message for miles driven
    elif gallons_used <= 0: # Validate the gallons used
        print("Gallons used must be greater than zero. Please try again.") # Error message for the Gallons used
    elif cost_per_gallon <= 0: # validate the cost per gallon
        print("Cost per gallon must be greater than zero. Please try again.") # Error message for the cost per gallon
    else: # If all variables are valid run the following
        # calculate and display miles per gallon
        mpg = round((miles_driven / gallons_used), 2) # Calculate the miles per gallon
        total_gas_cost = round((gallons_used * cost_per_gallon), 1) # Calculate the total cost
        cost_per_mile = round((total_gas_cost / miles_driven), 1) # Calculate the cost per mile
        print("Miles Per Gallon:\t\t", mpg) # Display the miles per gallon
        print("Total Gas Cost:\t\t\t", total_gas_cost) # Display the total cost
        print("Cost per Mile:\t\t\t", cost_per_mile) # Display the Cost per Mile
    print() # Print a blank line
    another_trip = input("Get entries for another trip (y/n)? ") # Offer the user to enter data again

    print() # Print a blank line
print("Bye") # Exit message



