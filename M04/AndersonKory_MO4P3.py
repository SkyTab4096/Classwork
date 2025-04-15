#Name: Kory Anderson
#Class: INFO 1200
#Section: 001
#Professor: Sharp
#Date: 2/14/25
#Assignment #: Project 4
#By submitting this assignment, I declare that the source code contained in this assignment was written #solely by me, unless specifically provided in the assignment. I attest that no part of this assignment, #in whole or in part, was directly created by Generative AI, unless explicitly stated in the assignment #instructions, nor obtained from a subscription service. I understand that copying any source code, #in whole or in part, unless specifically provided in the assignment, constitutes cheating, and that #I will receive a zero on this project if I am found in violation of this policy.

print("Kory Anderson's Change App") # Welcome message
print() # Prints a blank line

choice = "y" # Sets the default choice
while choice.lower() == "y": # Runs the code while the user wants to continue
    cents = int(input("Enter number of cents (0-99): ")) # Gathers the total cents to be divided
    print() # Prints a blank line

    quarters = round(cents // 25, 0) # Calculates the number of quarters to be handed out
    cents = cents % 25 # Removes the number of quarters from the total to be divided
    dimes = round(cents // 10, 0) # Calculates the number of dimes to be handed out
    cents = cents % 10 # Removes the number of dimes from the total to be divided
    nickels = round(cents // 5, 0) # Calculates the nickels to be handed out
    cents = cents % 5 # Removes the number of nickels from the total to be divided
    pennies = round(cents // 1, 0) # Calculates the pennies to be handed out
    cents = cents % 1 # Removes the number of pennies from the total to be divided
    
    print(f"Quarters:\t{quarters}") # Prints the number of quarters
    print(f"Dimes:\t\t{dimes}") # Prints the number of dimes
    print(f"Nickels:\t{nickels}") # Prints the number of nickels
    print(f"Pennies:\t{pennies}") # Prints the number of pennies
    
    print() # Prints a blank line
    choice = input("Continue? (y/n): ") # Prompts the user to continue using the app
print() # Prints a blank line
print("Bye!") # Exit message