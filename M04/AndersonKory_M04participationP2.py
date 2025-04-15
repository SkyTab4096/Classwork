#!/usr/bin/env python3

# display a welcome message
print("Welcome to Kory Anderson's Future Value Calculator") # Welcome message
print() # Print a blank line

choice = "y" # Default choice
while choice.lower() == "y": # While the user wants to enter more data run the following
    is_valid = False # Set the validation variable

    while is_valid == False: # If validation is false run the validation
        # get input from the user
        monthly_investment = float(input("Enter monthly investment:\t")) # Grab and store the monthly investment

        if monthly_investment <= 0 or monthly_investment > 1000: # Validate the monthly investment
            print("The monthly investment must be greater than 0 and less than or equal to 1000.  Please try again") # Error message for monthly investment
        else: # Variable is valid
            is_valid = True # Set the validation variable
    is_valid = False # Reset the validation variable

    while is_valid == False: # If validation variable is false run the validation
        yearly_interest_rate = float(input("Enter yearly interest rate:\t")) # Grab and store the yearly interest rate

        if yearly_interest_rate <= 0 or yearly_interest_rate > 15: # Validate the yearly interest
            print("The yearly interest rate must be greater than 0 and equal to or less than 15. Please try again.") # Yearly interest Error message
        else: # Variable is valid
            is_valid = True # Set the validation variable
    is_valid = False # Reset the validation variable

    while is_valid == False: # If validation is false run the validation
        years = int(input("Enter number of years:\t\t")) # Grab and store the number of years

        if years > 0 and years <= 50: # Validate the number of years
            is_valid = True # Set the validation variable
        else: # Variable is invalid
            print("The years must be greater than 0 and less than or equal to 50. Please try again.") # Error message for the number of years
    is_valid = False # Reset the validation variable
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest_rate / 12 / 100 # Convert yearly interest rate into monthly interest rate
    months = years * 12 # Calculate the number of months

    # calculate the future value
    future_value = 0 # Set the future value
    for i in range(months): # Calculate the future value for each month
        future_value += monthly_investment # Add the months investment
        monthly_interest_amount = future_value * monthly_interest_rate # Calculate the amount of interest earned
        future_value += monthly_interest_amount # Calculate the post interest investment for each month

    # display the result
    print() # Print a blank line
    print("Future value:\t\t\t" + str(round(future_value, 2))) # Display the calculated future value
    print() # Print a blank line
    # see if the user wants to continue
    choice = input("Continue (y/n)? ") # Offer the user to continue using the app
    print() # print a blank line

print("Bye!") # Exit message
