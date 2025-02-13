#Name: Kory Anderson
#Class: INFO 1200
#Section: 001
#Professor: Sharp
#Date: 2/13/25
#Assignment #: Project 4
#By submitting this assignment, I declare that the source code contained in this assignment was written #solely by me, unless specifically provided in the assignment. I attest that no part of this assignment, #in whole or in part, was directly created by Generative AI, unless explicitly stated in the assignment #instructions, nor obtained from a subscription service. I understand that copying any source code, #in whole or in part, unless specifically provided in the assignment, constitutes cheating, and that #I will receive a zero on this project if I am found in violation of this policy.

print("Kory Anderson's Letter Grade Converter") # Welcome message
print() # Prints a blank line

choice = "y" # Sets the default choice
while choice.lower() == "y": # Runs the following code while the user wants to continue
    number = int(input("Enter numerical grade: ")) # Gathers grade from user
    letter = "" # Sets a default letter grade

    if number > 100: # Validates if numeric grade is over 100
        print("Grades should be entered as a percentage and can't be greater than 100%. Please try again.") # Error message too high
    elif number >= 94 and number <= 100: # Checks for an A
        letter = "A" # Sets the letter grade to A
    elif number >= 90 and number < 94: # Checks for an A-
        letter = "A-" # Sets the letter grade to A-
    elif number >= 87 and number < 90: # Checks for a B+
        letter = "B+" # Sets the letter grade to B+
    elif number >= 84 and number < 87: # Checks for a B
        letter = "B" # Sets the letter grade to a B
    elif number >= 80 and number < 84: # Checks for a B-
        letter = "B-" # Sets the letter grade to a B-
    elif number >= 77 and number < 80: # Checks for a C+
        letter = "C+" # Sets the letter grade to a C+
    elif number >= 74 and number < 77: # Checks for a C
        letter = "C" # Sets the letter grade to a C
    elif number >= 70 and number < 74: # Checks for a C-
        letter = "C-" # Sets the letter grade to a C-
    elif number >= 67 and number < 70: # Checks for a D+
        letter = "D+" # Sets the letter grade to a D+
    elif number >= 64 and number < 67: # Checks for a D
        letter = "D" # Sets the letter grade to a D
    elif number >= 60 and number < 64: # Checks for a D-
        letter = "D-" # Sets the letter grade to a D-
    elif number >= 0 and number < 60: # Checks for a E
        letter = "E" # Sets the letter grade to a E
    else: # Validates if numeric grade is less than 0
        print("Grades should be entered as a percentage and can't be less than 0%. Please try again.") # Error message too low
    
    if letter != "": # Makes sure that the letter grade is not null
        print("Letter grade: ", letter) # Prints the letter grade
        print() # Prints a blank line
        choice = input("Continue? (y/n): ") # Asks the user if they want to continue
print() # Prints a blank line
print("Bye!") # Exit Message