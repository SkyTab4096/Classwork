# Kory Anderson validation file for the Future Value App
def get_float(prompt, low, high): # Define a function to validate a float value
    while True: # Run while the value is not within the desired range
        number = float(input(prompt)) # Prompt the user for a number
        if number > low and number <= high: # Check to see if the number is in the desired range
            return number # If valid use the number
        else: # If not valid reprompt the user and display a failure message
            print(f"Entry must be greater than {low} and less than {high}") # Failure message

def get_int(prompt, low, high): # Define a function to validate a integer value
    while True: # Run while the user inputs an invalid number
        number = int(input(prompt)) # Prompt the user for a number
        if number > low and number <= high: # Check to see if the number is in the desired range
            return number # If valid use the number
        else: # If not valid reprompt the user and display a failure message
            print(f"Entry must be greater than {low} and less than {high}") # Failure message

def main(): # Define the main part of the program
    choice = "y" # Set a default choice
    while choice.lower() == "y": # While the user wants to continue run the following
        valid_number = get_float("Enter number:", 0, 1000) # Prompt and validate a float number
        print(f"Valid Number = {valid_number}") # Display the valid number
        valid_int = get_int("Enter integer: ", 0, 50) # Prompt and validate an integer
        print(f"Valid Integer = {valid_int}") # Display the valid integer
        print() # Print a blank line
        choice = input("Repeat? (y/n): ") # Prompt the user to continue
    print("Bye!") # Exit message
if __name__ == "__main__": # Run the main part of the program only if the file is run directly
    main() # Run the main part of the program