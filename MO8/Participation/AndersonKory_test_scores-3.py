#!/usr/bin/env python3

def display_welcome(): # Defines a function to display a welcome message
    print("The Test Scores program") # Prints the title of the application
    print("Enter 'x' to exit") # Defines how to exit the program
    print("") # Prints a blank line

def get_scores(): # Defines a function to get the test scores from the user
    scoreList = [] # Makes an empty array for the test scores
    while True: # Makes a loop for entering test scores
        score = input("Enter test score: ") # Gets a test score from the user and stores it as a variable
        if score == "x": # If the entered value is the exit character run the following
            scoreList.sort() # Sort the list of test scores
            return  scoreList # Returns the sorted list to the program that called this function
        else: # If the exit character was not entered run the following
            score = getInt(score) # Calls a function to verify the score is an integer
            if score >= 0 and score <= 100: # Verifies that the score is within the boundaries
                scoreList.append(score) # Adds the score to the score array
            else: # If the score is not within the specified range
                print("Test score must be from 0 through 100.\nScore discarded. Try again.") # Prints an error message

def getInt(score): # Defines a function to verify that the entered test score is an integer
    try: # When called try running the following code
        return int(score) # Trys to return the passed score as an integer
    except ValueError: # If there was an error when converting the score into an integer, run the following
        print("Score entered is not an integer.\nScore discarded.  Please try again.") # Prints an error message

def process_scores(scoreList): # Defines a function to process the list of scores
    length = len(scoreList) # Stores the length of the list
    scoreTotal = 0 # Initializes the total score as 0
    medianScores = [] # Initializes a new list to store the median scores
    for i in scoreList: # For every value in the score list, 
        scoreTotal += i # Add that value to the total score
    averageScore = round(scoreTotal / length, 0) # Calculates the average score, rounding to the nearest integer
    minScore = min(scoreList) # Finds the minimum score
    maxScore = max(scoreList) # Finds the maximum score
    medianIndex = length / 2 # Finds the middle number in the score list
    if medianIndex % 2 != 0: # If the median index is not even run the following
        medianIndex = getInt(medianIndex - .5) # Restore the median index value as an integer 
        medianScore = scoreList[medianIndex] # Grabs the score in the score list at the median index value
    else: # If the median index is odd, run the following
        medianIndex1 = int(medianIndex - .5) # Stores a new median index, that is the next lowest integer from the median index value
        medianIndex2 = int(medianIndex + .5) # Stores a new median index, that is the next highest integer from the median index value
        medianScores.append(scoreList[medianIndex1]) # Stores the first median score in a list of median scores
        medianScores.append(scoreList[medianIndex2]) # Stores the second median score in a list of median scores
        medianScores.sort() # Sorts the list of median scores

    print() # Prints a blank line
    print(f"Score total:\t\t{scoreTotal}") # Displays the total score
    print(f"Number of Scores:\t{length}") # Displays the length of the score list
    print(f"Average Score:\t\t{averageScore}") # Displays the calculated average score
    print(f"Minimum Score:\t\t{minScore}") # Displays the minimum entered score
    print(f"Maximum Score:\t\t{maxScore}") # Displays the maximum entered score
    if len(medianScores) == 0: # Checks to see if a value was added to the median scores list
        print(f"Median Score:\t\t{medianScore}") # Prints the singular median score, if nothing was added to the median scores list
    else: # If a value was added to the median scores list, run the following
        intialString = str(medianScores) # Turns the median scores list into a string
        partialString = intialString.replace("[", "") # Removes the left bracket from the previously defined string
        medianScoresString = partialString.replace("]", "") # Removes the right bracket from the above string
        print(f"Median Scores:\t\t{medianScoresString}") # Prints the new string without the brackets

def main(): # Defines a function to run when the program starts 
    display_welcome() # Calls the function display the welcome message
    scoreList = get_scores() # Stores a list of the scores from the user
    process_scores(scoreList) # Passes that list of scores to the process scores function for processing
    print("\nBye!") # Prints a exit message

if __name__ == "__main__": # If the program is run standalone run the following
    main() # Calls the main function