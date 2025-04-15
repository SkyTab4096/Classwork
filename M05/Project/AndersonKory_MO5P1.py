#Name: Kory Anderson
#Class: INFO 1200
#Section: 001
#Professor: Sharp
#Date: 
#Assignment #: 5
#By submitting this assignment, I declare that the source code contained in this assignment was written #solely by me, unless specifically provided in the assignment. I attest that no part of this assignment, #in whole or in part, was directly created by Generative AI, unless explicitly stated in the assignment #instructions, nor obtained from a subscription service. I understand that copying any source code, #in whole or in part, unless specifically provided in the assignment, constitutes cheating, and that #I will receive a zero on this project if I am found in violation of this policy.

def is_even(num): # Define a new fuction called 'is_even'
    if num % 2 != 0: # Check to see if the number is divisable by 2
        return False # Tell if the number is not divisable by 2
    else: # Other case
        return True # Tell if number is divisable by 2

def main(): # Define a new function called 'main'
    print("Kory's even or odd checker") # Welcome message
    print() # Print a blank line
    choice = "y" # Add a choice variable to run multiple times
    while choice.lower() == "y": # While the user wants to continue run the following code
        myNum = int(input("Enter an integer: ")) # Get a number from the user
        if is_even(myNum) == True: # Check weither the number is even or not
            print("This is an even number.") # Tell the user the number is even
        else: # Other case
            print("This is an odd number.") # Tell the user the number is odd
        choice = input("Continue? (y/n):") # Prompt the user to continue

if __name__ == "__main__": # Run the code only if running the file directly
    main() # Runs the program