import tkinter as tk # Imports a basic gui application library 
from tkinter import ttk, messagebox # Imports some functions from that previously imported library
 
class testScoresFrames(ttk.Frame): # Defines the main frame that will house the entire program
    def __init__(self, parent): # Tells the frame what to do when initializing
        ttk.Frame.__init__(self, parent) # Calls the initializtion function for a frame

        testScoresFrame(parent).grid(row=0, column=0) # Creates a frame that houses the program

        ttk.Button(parent, text="Exit", command=parent.destroy).grid(column=1, row =2, sticky=tk.E, padx=15, pady=10) # Creates an exit button

class testScoresFrame(ttk.Frame): # Defines the frame that houses the application
    def __init__(self, parent): # Tells the frame what to do when initializing
        ttk.Frame.__init__(self, parent) # Calls the initialization function for a frame
        self.parent = parent # Stores that the parent of this frame is the parent that is passed from what called this
        self.message = "" # Initializes the error message variable

        self.testScore = [tk.StringVar()] # Intializes the test score variable as an array
        self.length = tk.StringVar() # Intializes the length variable
        self.avgScore = tk.StringVar() # Initializes the average score variable
        self.minScore = tk.StringVar() # Initializes the minimum score variable
        self.maxScore = tk.StringVar() # Initializes the maximum score variable
        self.medianScore = tk.StringVar() # Initializes the median score variable
        self.counter =tk.StringVar() # Initializes a counter variable

        self.initComponents() # Calls a function to create the initial gui components
    
    def clear(self): # Defines a function to clear all entered and displayed values
        self.testScore.set("") # Clears the test score value
        self.length.set("") # Clears the length value
        self.avgScore.set("") # Clears the average score value
        self.minScore.set("") # Clears the minimum score value
        self.maxScore.set("") # Clears the maximum score value
        self.medianScore.set("") # Clears the median score value
        self.counter.set("") # Clears the counter value
    
    def makeTestScore(self): # Defines a function to add an entry for a test score
        counter = self.counter.get() # Pulls the counter that is stored in the frame
        if counter == "": # If there is no value in the counter
            counter = 1 # Set the counter to one
        else: # If there was a value in the counter,
            counter = int(counter) # Turn the counter into a integer
            counter += 1 # Add one to the counter
        self.testScore.append(tk.StringVar()) # Add a new value to the test score array
        ttk.Label(self, text="Test Score:").grid(column=0, row=counter, sticky=tk.E, padx=5, pady=3) # Create a label for the new test score on the next row down
        ttk.Entry(self, width=25, textvariable=self.testScore[counter]).grid(column=1, row=counter, padx=5, pady=3) # Creates an entry for the user to add a test score

        counter = str(counter) # Converts the counter back to a string
        self.counter.set(f"{counter}") # Stores the counter back into the frame

    def initComponents(self): # Defines the function to initialize all the components of the gui
        ttk.Label(self, text="Test Score:").grid(column=0, row=0, sticky=tk.E) # Creates a label for the first test score entry
        ttk.Entry(self, width=25, textvariable=self.testScore[0]).grid(column=1, row=0) # Creates the first test score entry

        ttk.Label(self, text="Amount of Scores Entered:").grid(column=2, row=0, sticky=tk.E) # Creates a label for the amount of scores entered
        ttk.Entry(self, width=25, textvariable=self.length).grid(column=3, row=0) # Creates the place that the length is displayed to the user

        ttk.Label(self, text="Average Test Score:").grid(column=2, row=1, sticky=tk.E) # Creates a label for the average test score
        ttk.Entry(self, width=25, textvariable=self.avgScore).grid(column=3, row=1) # Creates the place that the average test score is displayed to the user

        ttk.Label(self, text="Minimum Test Score:").grid(column=2, row=2, sticky=tk.E) # Creates the label for the minimum entered test score
        ttk.Entry(self, width=25, textvariable=self.minScore).grid(column=3, row=2) # Creates the place that the minimum entered test score is displayed to the user

        ttk.Label(self, text="Maximum Test Score:").grid(column=2, row=3, sticky=tk.E) # Creates the label for the maximum entered test score
        ttk.Entry(self, width=25, textvariable=self.maxScore).grid(column=3, row=3) # Creates the place that the maximum score is displayed to the user

        ttk.Label(self, text="Median Test Score(s):").grid(column=2, row=4, sticky=tk.E) # Creates the label for the median entered test score
        ttk.Entry(self, width=25, textvariable=self.medianScore).grid(column=3, row=4) # Creates the place that the median test score(s) are displayed to the user

        self.makeButtons() # Call a function to create the nessicary buttons

        for child in self.winfo_children(): # Adds spacing to every item created in this function
            child.grid_configure(padx=5, pady=3) # Adds the spacing to the afore mentioned items
    
    def makeButtons(self): # Defines the function to create the nessicary buttons for the program
        buttonFrame = ttk.Frame(self) # Creates a standard frame for the button

        buttonFrame.grid(column=2, row=5, columnspan=2, sticky=tk.E) # Places the buttons in a standard location

        ttk.Button(buttonFrame, text="Clear", command=self.clear).grid(column=0, row=0, padx=5) # Adds the clear button
        ttk.Button(buttonFrame, text="Calculate", command=self.calculate).grid(column=1, row=0, padx=5) # Adds the calculate button
        ttk.Button(buttonFrame, text="Add Test Score", command=self.makeTestScore).grid(column=2, row=0) # Adds the button to make a new entry for the test scores
    
    def getInt(self, val, fieldName): # Defines a function to verify integers
        try: # When ran try this code
            return int(val) # Return the passed value as an integer
        except ValueError: # If there was an error when running the above code, run the following
            self.message += f"{fieldName} must be a valid integer" # Adds an error message to be displayed
    
    def calculate(self): # Defines a function to calculate and process the test scores
        self.message = "" # Re-initialize the error message variable

        testScores = [] # Create an array variable for the test scores
        counter = int(self.counter.get()) # Pull the counter from the parent frame
        for i in range(0, counter + 1): # For every value in the counter, run the following
            testScores.append(self.getInt(self.testScore[i].get(), "Test Score")) # Add the test score from the entrys, into a new array

        if self.message == "":
            length = len(testScores)
            testScores.sort()
            totalScore = 0
            medianScore = []
            for i in testScores:
                totalScore += i
            avgScore = totalScore / length
            minScore = min(testScores)
            maxScore = max(testScores)
            medianIndex = length / 2
            if medianIndex % 2 != 0:
                medianIndex = int(medianIndex - .5)
                medianScore.append(testScores[medianIndex])
            else:
                medianIndex1 = int(medianIndex - .5)
                medianIndex2 = int(medianIndex + .5)
                medianScore.append(testScores[medianIndex1])
                medianScore.append(testScores[medianIndex2])
            self.length.set(length)
            self.avgScore.set(avgScore)
            self.minScore.set(minScore)
            self.maxScore.set(maxScore)
            self.medianScore.set(medianScore)
        else:
            messagebox.showerror("Error", self.message)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Test Scores App")
    testScoresFrames(root)
    root.mainloop()            