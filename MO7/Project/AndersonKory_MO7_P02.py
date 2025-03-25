#!/usr/bin/env python3

#Name: Kory Anderson
#Class: INFO 1200
#Section: 001
#Professor: Sharp
#Date: April 2, 2025
#Assignment #: 7
#By submitting this assignment, I declare that the source code contained in this assignment was written #solely by me, unless specifically provided in the assignment. I attest that no part of this assignment, #in whole or in part, was directly created by Generative AI, unless explicitly stated in the assignment #instructions, nor obtained from a subscription service. I understand that copying any source code, #in whole or in part, unless specifically provided in the assignment, constitutes cheating, and that #I will receive a zero on this project if I am found in violation of this policy.

import tkinter as tk # Import a basic gui application library
from tkinter import ttk # Import the basic gui application toolkit from the library
import random # Import the random library

class applicationFrames(ttk.Frame): # Define a broad frame to contain the entire application
    def __init__(self, parent): # Define the initial function to run
        ttk.Frame.__init__(self, parent) # Declare that this is a frame

        applicationFrame(parent).grid(column=0, row=0) # Call the application frame and place it on the grid

        ttk.Button(parent, text="Exit", command=parent.destroy).grid(column=1, row=2, sticky=tk.E, padx=15, pady=10) # Make an exit button

class applicationFrame(ttk.Frame): # Define a frame to contain the application
    def __init__(self, parent): # Define the initial function to run in the frame
        ttk.Frame.__init__(self, parent) # Declare this as a frame
        self.parent = parent # Set the parent to be the parent of the frame
        self.message = "" # Clear any error messages

        self.length = tk.StringVar() # Initialize the length variable of the passcode
        self.passcode = tk.StringVar() # Initialize the passcode variable

        self.initComponents() # Call a function to initialize the application

    def initComponents(self): # Define the function to initialize the applicateion
        ttk.Label(self, text="Password Length:").grid(column=0, row=0, sticky=tk.E) # Make a label for the the length text box
        ttk.Entry(self, width=25, textvariable=self.length).grid(column=1, row=0) # Make a text box to enter the length

        ttk.Label(self, text="Generated Passcode:").grid(column=0, row=1, sticky=tk.E) # Make a label for the passcode text box
        ttk.Entry(self, width=25, textvariable=self.passcode).grid(column=1, row=1) # Make a text box to display the passcode

        self.makeButtons() # Call a function to make the clear and generate functions

        for child in self.winfo_children(): # For every item in the frame add spacing
            child.grid_configure(padx=5, pady=3) # Add the spacing to every item

    def makeButtons(self): # Define the function to create the buttons for the application
        buttonFrame = ttk.Frame(self) # Define a standard frame for each button

        buttonFrame.grid(column=0, row=3, columnspan=2, sticky=tk.E) # Make a standard placement of the buttons

        ttk.Button(buttonFrame, text="Clear", command=self.clear).grid(column=0, row=0, padx=5) # Create the first button to clear the text boxes
        ttk.Button(buttonFrame, text="Generate", command=self.generate).grid(column=1, row=0) # Create the second button to generate the passcode

    def clear(self): # Define the function to clear the text boxes
        self.length.set("") # Clear the length text box
        self.passcode.set("") # Clear the passcode text box
    
    def generate(self): # Defines the function to generate the passcode
        self.message = "" # Clears any error messages

        length = int(self.length.get()) # Define the length as the value within the length text box
        minLength = 10 ** (length - 1) # Make a minimum length
        maxLength = 10 ** length # Make a maximum length
        passcode = random.randint(minLength, maxLength - 1) # Generate the passcode

        self.passcode.set(passcode) # Set the passcode into the passcode text box
 
if __name__ == "__main__": # Run if running standalone
    root = tk.Tk() # Create a standard frame
    root.title("Passcode Generator") # Set the title of the application
    applicationFrames(root) # Call the broad frame to run the application
    root.mainloop() # Loop the application