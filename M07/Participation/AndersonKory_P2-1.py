#!/usr/bin/env python3

import tkinter as tk # Import one of the gui libraries
from tkinter import ttk, messagebox # Import more of the gui libraries
import locale # Import a localization library

from AndersonKory_P22 import Calculation # Import the self-defined calculation function

class calculatorFrames(ttk.Frame): # Create a broad root frame
    def __init__(self, parent): # Define the inital function of the frame
        ttk.Frame.__init__(self, parent) # Define the frame

        calculatorFrame(parent).grid(row=0, column=0) # Call the inner frame and add it to the grid

        ttk.Button(parent, text="Exit", command=parent.destroy).grid( # Add an exit button
            row=1, column=1, sticky=tk.E, padx=15, pady=10) # Add an exit button part 2

class calculatorFrame(ttk.Frame): # Create a frame to contain the application
    def __init__(self, parent): # Define the inital function of the frame
        ttk.Frame.__init__(self, parent) # Claim that this is a frame
        self.parent = parent # Make the parent variable equal to the parent of the current frame
        self.Calculation = Calculation() # Define the Calculation function to be the self-defined function
        self.message = "" # Clear any error messages

        locale.setlocale(locale.LC_ALL, 'en_US') # Set the localization

        self.diameter = tk.StringVar() # Initialize the values to be entered
        self.circumference = tk.StringVar() # Initialize the values to be entered

        self.initCompenents() # Call the initialize compenents function

    def clear(self): # Define a function to clear the values
        self.diameter.set("") # Set the diameter parameter to clear
        self.circumference.set("") # Set the circumferenece parameter to be clear

    def initCompenents(self): # Define the initialize compenents function
        ttk.Label(self, text="Diameter").grid( # Create a label for the diameter input
            column=0, row=0, sticky=tk.E) # Part 2
        ttk.Entry(self, width=25, textvariable=self.diameter).grid( # Create the entry box for diameter 
            column=1, row=0) # Part 2

        ttk.Label(self, text="Circumference").grid( # Create a label for the circumference output
            column=0, row=1, sticky=tk.E) # Part 2
        ttk.Entry(self, width=25, textvariable=self.circumference).grid( # Create the output box for circumference
            column=1, row=1) # Part 2

        self.makeButtons() # Call a function to make the clear and calculate buttones

        for child in self.winfo_children(): # Spaces out every item in the grid
            child.grid_configure(padx=5, pady=3) # Values to space by

    def makeButtons(self): # Defines the function to make the buttons
        buttonFrame = ttk.Frame(self) # Define a standard frame for the button

        buttonFrame.grid(column=0, row=2, columnspan=2, sticky=tk.E) # Add the button frame to the grid

        ttk.Button(buttonFrame, text="Clear", command=self.clear).grid(column=0, row=0, padx=5) # Create the clear button
        ttk.Button(buttonFrame, text="Calculate", command=self.calculate).grid(column=1, row=0) # Create the calculate button

    def getFloat(self, val, fieldName): # Define a function to verify the number
        try: # Try this code when called
            return float(val) # Code to try
        except ValueError: # If there is an error run the following
            self.message += f"{fieldName} must be a valid number" # Adds an error message to be displayed
    
    def calculate(self): # Defines a calculate function
        self.message = "" # Clears any left over error messages

        self.Calculation.diameter = self.getFloat(self.diameter.get(), "Diameter") # Sets the diameter in the imported function to be the entered diameter after verifying

        if self.message == "": # If no errors
            self.circumference.set(self.Calculation.calculate()) # Set the circumference box
        else: # If an error
            messagebox.showerror("Error", self.message) # Display the error

if __name__ == "__main__": # When running standalone
    root = tk.Tk() # Defines the root of the application
    root.title("Circle Calculator") # Sets the title of the application
    calculatorFrames(root) # Calls the function to display the application
    root.mainloop() # Loops the application 