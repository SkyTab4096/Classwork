#!/usr/bin/env python3

import csv # Imports the csv library to both write and read csv files

def getMilesDriven(): # Defines a function to get the miles driven from the user
    while (milesDriven := float(input("Enter miles driven:\t"))) <= 0: # Checks to see if the value the user entered is valid          
        print("Entry must be greater than zero. Please try again.\n") # Prints an error message if the value is invalid
    return milesDriven # Returns the miles that the user entered
          
def getGallonsUsed(): # Defines a function to get the gallons used from the user
    while (gallonsUsed := float(input("Enter gallons of gas:\t"))) <= 0: # Checks to see if the value the user entered is valid            
        print("Entry must be greater than zero. Please try again.\n") # Displays an error message if the value is invalid
    return gallonsUsed # Returns the gallons that the user entered to original function

def writeTrips(trips, filename='trips.csv'): # Defines a function to create the trips.csv file
        with open(filename, 'w', newline='') as csvfile: # Opens the file in write mode
            writer = csv.writer(csvfile) # Defines the writer that will write the data passed through to it
            writer.writerows(trips) # Tells the writer what to actually write

def readTrips(trips, filename='trips.csv'): # Defines a function to read the trips.csv file and store it as a variable
    with open(filename, 'r') as file: # Opens the file in read mode
        csvReader = csv.reader(file) # Creates the reader to read the csv file
        for row in csvReader: # For every row in the file do the following
            if len(trips[0]) == 0: # Checks to see if any data has been entered into the 2d array
                trips[0] = row # If no data was entered into the 2d array then replace the first row with the first line of the file
            else: # If there has been data entered into the 2d array run the following
                trips.append(row) # Add a new row in the 2d array with the row in the file
        return trips # Once all rows have been read and stored, return the new 2d array to the original function

def listTrips(filename='trips.csv'): # Defines a new function to print every row in the csv file
    print(f'Miles, Gallons, MPG') # Display column titles for the data in the csv file
    with open(filename, 'r') as file: # Opens the csv file in read mode
        csvReader = csv.reader(file) # Creates the reader to read the csv file
        for row in csvReader: # For every row in the file, run the following
            print(row) # Print the row
    print() # Print a new blank spacer line

def main(): # Define the main function of the program
    print("The Miles Per Gallon program\n") # Displays the title of the program

    trips = [[]] # Creates the 2d array/Clears the array if it already exists
    more = "y" # Defines the standard choice for the loop of the main function
    while more.lower() == "y": # If the user wants to continue or on the first loop the standard choice is set, run the following
        trips = readTrips(trips, 'trips.csv') # Redefines the 2d array as the information in the csv file
        listTrips('trips.csv') # Display the information in the csv file to the user
        milesDriven = getMilesDriven() # Get the miles driven from the user
        gallonsUsed = getGallonsUsed() # Get the gallons used from the user
                                 
        mpg = round((milesDriven / gallonsUsed), 2) # Calculate the miles per gallon from the values the user entered
        if len(trips[0]) == 0: # Checks to see if there is any information in the 2d array
            trips[0] = [milesDriven, gallonsUsed, mpg] # If there is no information stored, replace the first row with the information entered
        else: # If any information has been stored,
            trips.append([milesDriven, gallonsUsed, mpg]) # Create a new row with the information entered

        print(f"Miles Per Gallon:\t{mpg}\n") # Display the calculated miles per gallon to the user
        
        writeTrips(trips, 'trips.csv') # Overite the csv file with the new information
        listTrips('trips.csv') # List the trips in the trips.csv file

        more = input("More entries? (y or n): ") # Prompts the user if they want to continue

    print("Bye!") # Prints an exit message to the user

if __name__ == "__main__": # If running the program standalone,
    main() # Call the main function of the program