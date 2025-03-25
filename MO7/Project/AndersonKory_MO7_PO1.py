#Name: Kory Anderson
#Class: INFO 1200
#Section: 001
#Professor: Sharp
#Date: April 2, 2025
#Assignment #: 7
#By submitting this assignment, I declare that the source code contained in this assignment was written #solely by me, unless specifically provided in the assignment. I attest that no part of this assignment, #in whole or in part, was directly created by Generative AI, unless explicitly stated in the assignment #instructions, nor obtained from a subscription service. I understand that copying any source code, #in whole or in part, unless specifically provided in the assignment, constitutes cheating, and that #I will receive a zero on this project if I am found in violation of this policy.

import tkinter as tk # Import a basic GUI library
from tkinter import ttk, messagebox # Import basic features from a GUI library
import math # Import the math library to calculate square roots

class pythagoreanFrames(ttk.Frame): # Define a broad frame to contain the whole application
    def __init__(self, parent): # Define the initialization function
        ttk.Frame.__init__(self, parent) # Declare that this is a frame

        pythagoreanFrame(parent).grid(row=0, column=0) # Call the application frame

        ttk.Button(parent, text="Exit", command=parent.destroy).grid(column=1, row=2, sticky=tk.E, padx=15, pady=10) # Add a exit button

class pythagoreanFrame(ttk.Frame): # Define a frame for the application
    def __init__(self, parent): # Define the initialization function for the application
        ttk.Frame.__init__(self, parent) # Declare that this is a frame
        self.parent = parent # Set that the parent frame of this frame is in fact the parent of this frame
        self.message = "" # Initialize the error message variable

        self.base = tk.StringVar() # Initialize the variable used to store the base of the triangle
        self.height = tk.StringVar() # Initialize the variable used the store the height of the triangle
        self.hypotenuse = tk.StringVar() # Initialize the variable used to store the hypotenuse of the triangle

        self.initComponents() # Call the function to make the labels, text boxes, and buttons

    def clear(self): # Define a function to clear the variables
        self.base.set("") # Clear the base of the triangle
        self.height.set("") # Clear the height of the triangle
        self.hypotenuse.set("") # Clear the hypotenuse of the triangle

    def initComponents(self): # Define the function to make the labels, text boxes, and buttons
        ttk.Label(self, text="Base of the triangle:").grid(column=0, row=0, sticky=tk.E) # Create the label for the text box input for the base of the triangle
        ttk.Entry(self, width=25, textvariable=self.base).grid(column=1, row=0) # Create the text box input for the base of the triangle

        ttk.Label(self, text="Height of the triangle:").grid(column=0, row=1, sticky=tk.E) # Create the label for the text box input for the height of the triangle
        ttk.Entry(self, width=25, textvariable=self.height).grid(column=1, row=1) # Create the text box input for the height of the triangle

        ttk.Label(self, text="Hypotenuse of the triangle:").grid(column=0, row=2, sticky=tk.E) # Create the label for the text box output of the hypotenuse of the triangle
        ttk.Entry(self, width=25, textvariable=self.hypotenuse).grid(column=1, row=2) # Create the text box output for the hypotenuse of the triangle

        self.makeButtons() # Call the function to make the buttons

        for child in self.winfo_children(): # For every item in this function, run this code to space them out
            child.grid_configure(padx=5, pady=3) # Space out every item 
    
    def makeButtons(self): # Defines the function to make the buttons
        buttonFrame = ttk.Frame(self) # Defines a standatd frame for the buttons

        buttonFrame.grid(column=0, row=3, columnspan=2, sticky=tk.E) # Sets a standard location for the buttons

        ttk.Button(buttonFrame, text="Clear", command=self.clear).grid(column=0, row=0, padx=5) # Creates the first button to clear all the inputs, using the clear function from earlier
        ttk.Button(buttonFrame, text="Calculate", command=self.calculate).grid(column=1, row=0) # Creates the second button to calculate the hypotenuse of the triangle

    def getInt(self, val, fieldName): # Defines a function to verify if a number is an integer
        try: # When called run the following code
            return int(val) # Attempt to turn the passed value into an integer
        except ValueError: # If the above code runs into an error run the following
            self.message += f"{fieldName} must be a valid integer" # Add an error message

    def calculate(self): # Defines the function used to calculate the hypotenuse
        self.message = "" # Clears any existing error messages

        base = self.getInt(self.base.get(), "Base") # Stores the base of the triangle, also verifies that it is an integer
        height = self.getInt(self.height.get(), "Height") # Stores the height of the triangle, also verifies that it is an integer

        if self.message == "": # If there was no error run the following
            hypotenuse = round(math.sqrt(base ** 2 + height ** 2), 3) # Calculate the hypotenuse
            self.hypotenuse.set(hypotenuse) # Set the hypotenuse box
        else: # If there was an error, display the error message
            messagebox.showerror("Error", self.message)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Pythagorean Theorem Calculator")
    pythagoreanFrames(root)
    root.mainloop()