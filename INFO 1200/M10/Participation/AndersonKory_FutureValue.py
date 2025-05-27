#!/usr/bin/env python3
            
def getNumber(prompt, low, high): # Defines a function to get a number from the user and handle if the number is invalid
    while True: # Defines a loop to run until the user enters a valid input
        number = input(prompt) # Gets the input from the user
        try: # Run the next block of code every time the function is called
            number = float(number) # Attempts to turn the entered number into a floating point number
            if number > low and number <= high: # Checks to see if the entered value is within the specified limits
                return number # Return the entered number to the function that called this function
            else: # If not within the specified limits, print an error message
                print(f"Entry must be greater than {low} and less than or equal to {high}") # Display said error message 
        except ValueError: # If there was an error when turning the entered value into a number run the following
            print(f"Please enter a valid number") # Prints an error message

def getInteger(prompt, low, high): # Defines a function to get an integer from the user and check to make sure that it's valid
    while True: # Defines a loop to run until the user enters a valid input
        number = input(prompt) # Gets an input from the user
        try: # Run the next block of code every time the function is called
            number = int(number) # Attempts to turn the entered value into an integer
            if number > low and number <= high: # Checks to see if the entered value is wihtin specified limits
                return number # Returns the entered value to the original function
            else: # If the entered number is not within the limits
                print(f"Entry must be greater than {low} and less than or equal to {high}") # Print this error message
        except ValueError: # If there was an error while turning the number into an integer
            print(f"Please enter a valid integer") # Display this error message

def calculate_future_value(monthly_investment, yearly_interest, years): # Defines a function to calculate the future value
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100 # Converts the entered yearly interest rate into a monthly interest rate
    months = years * 12 # Converts the entered number of years into months

    # calculate future value 
    future_value = 0.0 # Initalizes and clears a future value variable
    for i in range(months): # For every month
        future_value += monthly_investment # Add the monthly investment to the total
        monthly_interest = future_value * monthly_interest_rate # Calculate the monthly interest
        future_value += monthly_interest # Add the monthly interest

    return future_value # Return the calculated total to the original function

def main(): # Defines the main function of the program
    choice = "y" # Sets a default choice to run the program
    while choice.lower() == "y": # While the user wants to continue or the default choice was set
        # get input from the user
        monthly_investment = getNumber("Enter monthly investment:\t", 0, 1000) # Gets the monthly investment from the user
        yearly_interest_rate = getNumber("Enter yearly interest rate:\t", 0, 15) # Gets the yearly interest rate from the user
        years = getInteger("Enter number of years:\t\t", 0, 50) # Gets the number of years for the investment from the user

        # get and display future value 
        future_value = calculate_future_value(monthly_investment, yearly_interest_rate, years) # Calulates and stores the future value using all the entered values
        
        print(f"\nFuture value:\t\t\t{round(future_value, 2)}\n") # Displays the calculated future value to the user
        
        # see if the user wants to continue
        choice = input("Continue? (y/n): ") # Prompt the user if they want to continue
        print() # Print a spacing line

    print("Bye!") # Print an exit message
    
if __name__ == "__main__": # If running the program standalone, 
    main() # Call the main function of the program
