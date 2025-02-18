#Name: Kory Anderson
#Class: INFO 1200
#Section: 001
#Professor: Sharp
#Date: 
#Assignment #: 5
#By submitting this assignment, I declare that the source code contained in this assignment was written #solely by me, unless specifically provided in the assignment. I attest that no part of this assignment, #in whole or in part, was directly created by Generative AI, unless explicitly stated in the assignment #instructions, nor obtained from a subscription service. I understand that copying any source code, #in whole or in part, unless specifically provided in the assignment, constitutes cheating, and that #I will receive a zero on this project if I am found in violation of this policy.

def is_even(num):
    if num % 2 != 0:
        return False
    else:
        return True

def main():
    print("Kory's even or odd checker")
    print()
    choice = "y"
    while choice.lower() == "y":
        myNum = int(input("Enter an integer: "))
        if is_even(myNum) == True:
            print("This is an even number.")
        else:
            print("This is an odd number.")
        choice = input("Continue? (y/n):")

if __name__ == "__main__":
    main()