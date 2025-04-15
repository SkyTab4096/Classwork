#!/usr/bin/env python3
import validate as v # Import the validation program

print("Anderson's Validated Future Value App") # Welcome message
def calculate_future_value(monthly_investment, yearly_interest, years): # Define a function to calculate the future value
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100 # Calculate the monthly interest rate
    months = years * 12 # Calculate how many months to run the loop

    # calculate future value
    future_value = 0.0 # Set the future value to zero to prevent it from reusing previous values
    for i in range(0, months): # Run the following for each month
        future_value += monthly_investment # Add the monthly investment
        monthly_interest = future_value * monthly_interest_rate # Calculate the monthly interest
        future_value += monthly_interest # Add the previously calculated interest

    return future_value # Return the value calculated to the original program

def main(): # Define the main part of the program
    choice = "y" # Set a default choice to continue
    while choice.lower() == "y": # While the choice is to continue run the following
        # get input from the user
        monthly_investment = v.get_float("Enter monthly investment:\t", 0, 1000) # Get and store the monthly investment from the user
        yearly_interest_rate = v.get_float("Enter yearly interest rate:\t", 0, 15) # Get and store the yearly interest from the user
        years = v.get_int("Enter number of years:\t\t", 0, 50) # Get and store the number of years to run the calculation

        # get and display future value
        future_value = calculate_future_value( # Calculate the future value
            monthly_investment, yearly_interest_rate, years) # Pass the nessicary variables to the future value function

        print("Future value:\t\t\t" + str(round(future_value, 2))) # Display the Future value
        print() # Print a blank line

        # see if the user wants to continue
        choice = input("Continue? (y/n): ") # Prompt the user to continue
        print() # Print a blank line

    print("Bye!") # Exit message
    
if __name__ == "__main__": # Run the main part of the code only if the file is run directly
    main() # Run the main part of the code
