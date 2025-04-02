#Name: Kory Anderson
#Class: INFO 1200
#Section: 001
#Professor: Dr. Jason Sharp
#Date: April 9, 2025
#Assignment #: 8
#By submitting this assignment, I declare that the source code contained in this assignment was written #solely by me, unless specifically provided in the assignment. I attest that no part of this assignment, #in whole or in part, was directly created by Generative AI, unless explicitly stated in the assignment #instructions, nor obtained from a subscription service. I understand that copying any source code, #in whole or in part, unless specifically provided in the assignment, constitutes cheating, and that #I will receive a zero on this project if I am found in violation of this policy.

def displayTitle():
    print(f"Kory Anderson's Wizard Inventory Game")
    print()

def printMenu():
    print(f"COMMAND MENU\n")
    print(f"show - Show all items")
    print(f"grab - Grab an item")
    print(f"edit - Edit an item")
    print(f"drop - Drop an item")
    print(f"exit - Exit the program\n")

def show(inventory):
    for number, item in enumerate(inventory, start = 1):
        print(f"{number}. {item}\n")

def grabItem(inventory):
    if len(inventory) >= 4:
        print(f"You can't carry any more items.  Drop something first.\n")
    else:
        item = input("Name:\t")
        inventory.append(item)
        print(f"{item} was added.\n")

def editItem(inventory):
    number = int(input("Number:\t"))
    if number < 1 or number > len(inventory):
        print(f"Invalid number.  Please try again.")
    else:
        item = input("Updated name:\t")
        inventory[number-1] = item
        print(f"Item number {number} was updated.\n")

def dropItem(inventory):
    number = int(input("Number:\t"))
    if number < 1 or number > len(inventory):
        print(f"Invalid Number.  Please try again.\n")
    else:
        item = inventory.pop(number - 1)
        print(f"{item} was dropped.\n")

def main():
    displayTitle()
    printMenu()

    inventory = ["staff", "spellbook", "cloak"]

    while True:
        command = input("Command:\t")
        if command.lower() == "show":
            show(inventory)
        elif command.lower() == "grab":
            grabItem(inventory)
        elif command.lower() == "edit":
            editItem(inventory)
        elif command.lower() == "drop":
            dropItem(inventory)
        elif command.lower() == "exit":
            break
        else:
            print(f"Not a valid command. Please try again.\n")
    print(f"Bye!")

if __name__ == "__main__":
    main()