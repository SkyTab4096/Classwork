class Calculation(): # Defines a class for the calculation function
    diameter:float = 0.0 # Initializes the diameter variable
    
    def calculate(self): # Defines the calculate function
        if self.diameter != 0: # Makes sure that a value was entered
            pi = float(3.14159265359) # Defines pi to a number of decimal places
            radius = self.diameter / 2 # Calculates the radius of the circle
            circumference = 2 * pi * radius # Calculates the circumference of the circle

            return circumference # Returns the circumference
        
        else: # If no value was entered into the diameter box
            self.message += f"Diameter must not be empty" # Add an error message to be displayed