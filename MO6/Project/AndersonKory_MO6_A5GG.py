#!/usr/bin/env python3

#Name: Kory Anderson
#Class: INFO 1200
#Section: 001
#Professor: Sharp
#Date: March 24, 2025
#Assignment #: 6
#By submitting this assignment, I declare that the source code contained in this assignment was written #solely by me, unless specifically provided in the assignment. I attest that no part of this assignment, #in whole or in part, was directly created by Generative AI, unless explicitly stated in the assignment #instructions, nor obtained from a subscription service. I understand that copying any source code, #in whole or in part, unless specifically provided in the assignment, constitutes cheating, and that #I will receive a zero on this project if I am found in violation of this policy.

import random # Import the random library

def display_title(): # Defines a function to display the title
    print("Guess the number!") # Displays the title
    print() # Prints a blank line

def get_limit(): # Defines a function to get the limit of the game
    limit = int(input("Enter the upper limit for the range of numbers: ")) # Gets the limit from the user
    return limit # returns the limit gathered

def play_game(limit): # Defines the function for the game
    number = random.randint(1, limit) # Gets the random number
    count = 0 # Initializes the count variable to count guesses
    print(f"I'm thinking of a number from 1 to {limit}\n") # Let the user know that we are playing the game

    while True: # Starts a loop
        guess = int(input("Your guess: ")) # Gets a guess from the user
        if guess < number: # Checks the guess against the number
            print("Too low.") # Let's the user know if the guess was too low
            count += 1 # Increases the count
        elif guess > number: # Checks the guess against the number
            print("Too high.") # Let's the user know if the guess was too high
            count += 1 # Increases the count
        elif guess == number: # Checks to see if the user guessed the number
            print(f"You guessed it in {count} tries.\n") # Tells the user that they found the number and the total number of guesses
            break # Ends the loop

def main(): # Defines the main function
    display_title() # Calls the title function to display the title
    
    again = "y" # Initializes a choice variable
    while again.lower() == "y": # Begins a loop while the user wants to continue
        limit = get_limit() # Gets a limit variable
        play_game(limit) # Plays the game with the limit variable
        
        again = input("Play again? (y/n): ") # Prompts the user to continue
        print() # Prints a blank line
    print("Bye!") # Prints an exit message

# if started as the main module, call the main function
if __name__ == "__main__": # Used when running the file standalone
    main() # Calls the main function

