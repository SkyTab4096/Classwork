#Name: Kory Anderson
#Class: INFO 1200
#Section: 001
#Professor: Sharp
#Date: 2/14/25
#Assignment #: Project 4
#By submitting this assignment, I declare that the source code contained in this assignment was written #solely by me, unless specifically provided in the assignment. I attest that no part of this assignment, #in whole or in part, was directly created by Generative AI, unless explicitly stated in the assignment #instructions, nor obtained from a subscription service. I understand that copying any source code, #in whole or in part, unless specifically provided in the assignment, constitutes cheating, and that #I will receive a zero on this project if I am found in violation of this policy.

print("Kory Anderson's Tip Calculator") # Welcome message
print() # Prints a blank line

mealCost = float(input("Cost of Meal: ")) # Asks and stores the cost of the meal
print() # Prints a blank line

# The following code does not use a for loop because a for loop requires using either a list or an array.
#i = 0 # Sets an index counter
#while i < 3: # Only lets the loop run three times
#    if i == 0: # First iteration of the loop
#        print("15%") # Prints the tip percent
#        tip = 15 # Sets the tip portion
#        tipPercent = tip / 100 # Calculates the tip percent
#        tipAmount = round(mealCost * tipPercent, 2) # Calculates the tip amount
#        total = round(mealCost + tipAmount, 2) # Calculates the total
#        print(f"Tip Amount: {tipAmount}") # Prints the tip amount
#        print(f"Total Amount: {total}") # Prints the total
#    elif i == 1: # Second iteration of the loop
#        print("20%") # Prints the tip percentage
#        tip = 20 # Sets the tip portion
#        tipPercent = tip / 100 # Calculates the tip percent
#        tipAmount = round(mealCost * tipPercent, 2) # Calculates the tip amount
#        total = round(mealCost + tipAmount, 2) # Calculates the total cost
#        print(f"Tip Amount: {tipAmount}") # Prints the tip amount
#        print(f"Total Amount: {total}") # Prints the total amount
#    elif i == 2: # Third Iteration
#        print("25%") # Prints the tip percent
#        tip = 25 # Sets the tip portion
#        tipPercent = tip / 100 # Calculates the tip percentage
#        tipAmount = round(mealCost * tipPercent, 2) # Calculates the tip amount
#        total = round(mealCost + tipAmount, 2) # Calculates the total cost
#        print(f"Tip Amount: {tipAmount}") # Prints the tip amount
#        print(f"Total Amount: {total}") # Prints the total cost
#    i += 1 # Incriments the index counter

# The following code utilizes a for loop but also has an array.
for tip in [15, 20, 25]: # Runs the following code for each tip portion
    print(f"{tip}%") # Prints the tip percentage
    tipPercent = tip / 100 # Calculates the tip percent
    tipAmount = round(mealCost * tipPercent, 2) # Calculates the tip amount
    total = round(mealCost + tipAmount, 2) # Calculates the total cost

    print(f"Tip Amount: {tipAmount}") # Prints the tip amount
    print(f"Total Amount: {total}") # Prints the total cost