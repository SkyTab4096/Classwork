#Name: Kory Anderson
#Class: INFO 1200
#Section: 001
#Professor: Dr. Jason Sharp
#Date: April 9, 2025
#Assignment #: 8
#By submitting this assignment, I declare that the source code contained in this assignment was written #solely by me, unless specifically provided in the assignment. I attest that no part of this assignment, #in whole or in part, was directly created by Generative AI, unless explicitly stated in the assignment #instructions, nor obtained from a subscription service. I understand that copying any source code, #in whole or in part, unless specifically provided in the assignment, constitutes cheating, and that #I will receive a zero on this project if I am found in violation of this policy.

import tkinter as tk
from tkinter import ttk, messagebox

inventory = ["Staff", "Grimoire", "Cloak"]

class inventoryGameFrames(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        self.inventory = inventory
        self.commandsText = ["Grab", "Edit", "Drop"]
        self.commands = ["grabItem", "editItem", "dropItem"]

        for i in enumerate(self.inventory.get(), start=0):
            itemFrame(parent).grid(column=i, row=0, padx=15, pady=10)

        ttk.Button(parent, text="Grab", command=grabItem(self.inventory.get())).grid(column=0, row=1, sticky=tk.E, padx=5, pady=3)
        ttk.Button(parent, text="Edit", command=editItem(self.inventory.get())).grid(column=0, row=1, sticky=tk.E, padx=5, pady=3)
        ttk.Button(parent, text="Drop", command=dropItem(self.inventory.get())).grid(column=0, row=1, sticky=tk.E, padx=5, pady=3)

        ttk.Button(parent, text="Exit", command=parent.destroy).grid(column=1, row=2, sticky=tk.E, padx=15, pady=10)

        def grabItem(currentInventory):
            if len(currentInventory) >=4:
                message += "You can't carry any more items.  Drop something and try again."
            else:
                
                inventory.append(item)

class itemFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.message = ""

        self.item = tk.StringVar()

        
      
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Inventory Game")
    inventoryGameFrames(root)
    root.mainloop()