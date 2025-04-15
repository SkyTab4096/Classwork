#!/usr/bin/env python3

#Name: Kory Anderson
#Class: INFO 1200
#Section: 001
#Professor: Sharp
#Date: March 24, 2025
#Assignment #: 6
#By submitting this assignment, I declare that the source code contained in this assignment was written #solely by me, unless specifically provided in the assignment. I attest that no part of this assignment, #in whole or in part, was directly created by Generative AI, unless explicitly stated in the assignment #instructions, nor obtained from a subscription service. I understand that copying any source code, #in whole or in part, unless specifically provided in the assignment, constitutes cheating, and that #I will receive a zero on this project if I am found in violation of this policy.

tax = 0.06 # Sets a standard tax rate

def sales_tax(total): # Defines a function to calculate sales tax
    sales_tax = total * tax # Calculates sales tax
    return sales_tax # Gives the calculated value to the main function

def main(): # Defines the main function
    print("Sales Tax Calculator\n") # Prints an application title
    total = float(input("Enter total: ")) # Gathers the total from the user 
    total_after_tax = round(total + sales_tax(total), 2) # Calculates the total after tax and rounds to two decimal places
    print("Total after tax: ", total_after_tax) # Tells the user the calculated value
    
if __name__ == "__main__": # Used when running standalone
    main() # Calls the main function
