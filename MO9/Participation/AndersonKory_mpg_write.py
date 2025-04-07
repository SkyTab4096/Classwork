#!/usr/bin/env python3

import csv # Imports the library to write csv files

def getMilesDriven(): # Defines a function to get the miles driven from the user
    while (milesDriven := float(input("Enter miles driven:\t"))) <= 0: # Checks to see if the value the user enters is less than or equal to zero
        print("Entry must be greater than zero. Please try again.\n") # Prints an error message if the value the user entered is less than or equal to zero
    return milesDriven # Returns the value the user enters to the original function
          
def getGallonsUsed(): # Defines a function to get the gallons used from the user
    while (gallonsUsed := float(input("Enter gallons of gas:\t"))) <= 0: # Checks to see if the value the user enters is less than or equal to zero            
        print("Entry must be greater than zero. Please try again.\n") # Prints an error message to the user if the value entered is not valid
    return gallonsUsed # Returns the value the user entered to the original function

def outputCsv(data, filename='trips.csv'): # Defines a function to write the output file
    with open(filename, 'w', newline='') as csvfile: # Opens the file and says that we are writing to it
        writer = csv.writer(csvfile) # Makes the writer that will actually do the writing
        writer.writerows(data) # Tells the previously defined writer what to write

def main(): # Defines the main function for the program
    print("The Miles Per Gallon program\n") # Displays a title to the user
    
    tripInformation =[[]] # Intialize the 2d array that the information will be stored in
    more = "y" # Sets a default choice to run the program loop
    while more.lower() == "y": # Checks to see if the user wants to continue, or if the default choice was set
        milesDriven = getMilesDriven() # Gets the miles driven from the user
        gallonsUsed = getGallonsUsed() # Gets the gallons used from the user
                                 
        mpg = round((milesDriven / gallonsUsed), 2) # Calculates the miles per gallon with the entered information

        if len(tripInformation[0]) == 0: # Checks to see if any information has been saved to the 2d array
            tripInformation = [[milesDriven, gallonsUsed, mpg]] # If no information was saved set the first row to be the first set of entered an calculated information
        else: # If information was previously entered
            tripInformation.append([milesDriven, gallonsUsed, mpg]) # Add a new row to the array with the currently entered and calculated information
        
        print(f"Miles Per Gallon:\t{mpg}\n") # Display the calculated miles per gallon to the user
                
        more = input("More entries? (y or n): ") # Prompts the user if they want to continue
    
    outputCsv(tripInformation, 'trips.csv') # Calls the function to create/overwrite the output file
    print("Bye!") # Prints an exit message to the user

if __name__ == "__main__": # If the file is run standalone, run the following
    main() # Call the main function of the program