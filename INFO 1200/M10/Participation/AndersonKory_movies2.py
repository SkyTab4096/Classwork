import csv # Import the csv library to read and write csv files
import sys # Import the sys library to add the ability to stop the program early

FILENAME = "moview_test.csv" # Set a default file name for the list of movies

def getInt(prompt, low=0): # Defines a function to get an integer from the user and make sure it's a valid integer
    while True: # Defines a loop for the function
        try: # Defines what to do each time the code is run, with error handling
            integer = int(input(prompt)) # Attempt to turn the entered value into an integer
            if integer > low: # Check to make sure that the entered value is above the low end of the range
                return integer # If valid return the number
            else: # If the entered value does not meet the required standards print the following error message
                print(f"Number of years must be greater than zero") # Error message
        except ValueError: # If there was a problem when turning the entered value into an integer, run the following
            print(f"Please enter a valid integer") # Display an error message
            
def exit_program(): # Defines a function to exit the program
    print("Terminating program.") # Display a message when exitting
    sys.exit() # Exit the program

def read_movies(): # Defines a function to read the file that stores the movie list
    try: # Initialize a loop with built-in error handling
        movies = [] # Make an empty array to contain the information
        with open(FILENAME, newline="") as file: # Open the movie list file
            reader = csv.reader(file) # Create the reader to read the contents of the file
            for row in reader: # For every row that was found,
                movies.append(row) # Add it to the previously created array
        return movies # Return the list of movies
    except FileNotFoundError as e: # If there was specifically an error that the file couldn't be found, run the following
        #print(f"Could not find {fileName} file.")
        #exit_program()
        return movies # Return the empty array of movies so the program can keep running
    except Exception as e: # If there was a different error when running the code,
        print(type(e), e) # Tell the user what error occuried
        exit_program() # Exit the program

def write_movies(movies): # Defines a function to make the movie list file
    try: # Initialize a loop with built-in error handling
        with open(FILENAME, "w", newline="") as file: # Open the file to write
            writer = csv.writer(file) # Create the writer to write the data
            writer.writerows(movies) # Write the data in the movies array
        # raise BlockingIOError
    except Exception as e: # If there was an error
        print(type(e), e) # Tell the user what the error was
        exit_program() # Exit the program

def list_movies(movies): # Define a function to list the movies in the storage array
    for i, movie in enumerate(movies, start=1): # Make a loop to list the movies
        print(f"{i}. {movie[0]} ({movie[1]})") # List each individual movie
    print() # Print a spacing line
    
def add_movie(movies): # Define a function to add to the movie list
    name = input("Name: ") # Get the name from the user
    year = getInt("Year: ", 0) # Get the year the movie was released, also make sure it's an integer
    movie = [name, year] # Make an array with the entered information
    movies.append(movie) # Add the array to the current storage array
    write_movies(movies) # Re-write the movie list file
    print(f"{name} was added.\n") # Tell the user it was successful

def delete_movie(movies): # Define a function to remove a movie from the list
    while True: # Create a loop
        try: # Create a loop with error handling
            number = int(input("Number: ", 1)) # Get and verify that a number is a valid integer 
        except ValueError: # If there was an error while turning the entered number into an integer run the following
            print("Invalid integer. Please try again.") # Print an error message
            continue # Continue with the try loop
        if number < 1 or number > len(movies): # Check to make sure that the entered number is within the valid range
            print("There is no movie with that number. Please try again.") # Display an error message if the entered value is invalid
        else: # If the value entered is valid
            break # Stop the loop
    movie = movies.pop(number - 1) # Store the values in the array after removing the specified movie
    write_movies(movies) # Store the storage array into a file
    print(f"{movie[0]} was deleted.\n") # Inform the user that the specified movie was removed

def display_menu(): # Defines a function to display the command menu
    print("The Movie List program\n") # Title
    print("COMMAND MENU") # Menu title
    print("list - List all movies") # command 1
    print("add -  Add a movie") # Command 2
    print("del -  Delete a movie") # Command 3
    print("exit - Exit program\n") # Command 4

def main(): # Define the main function of the program
    movies = read_movies() # Store the contents of the storage file
    while True: # Define a command loop
        display_menu() # Display the command menu
        command = input("Command: ") # Get a command from the user
        if command.lower() == "list": # Checks to see if the entered command is the first command
            list_movies(movies) # Call the function to display the contents of the storage array
        elif command.lower() == "add": # Checks to see if the entered command is the second command
            add_movie(movies) # Calls the function to add a movie to the list
        elif command.lower() == "del": # Checks to see if the entered command is the third command
            delete_movie(movies) # Calls the function to delete a movie from the list
        elif command.lower() == "exit": # Checks to see if the entered command is the fourth command
            break # Stop the loop
        else: # If no valid command was entered
            print("Not a valid command. Please try again.\n") # Print an error message
    print("Bye!") # Print an exit message

if __name__ == "__main__": # If running the program standalone
    main() # Run the main function of the program