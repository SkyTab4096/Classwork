#!/usr/bin/env python3

#Name: Kory Anderson
#Class: INFO 1200
#Section: 001
#Professor: Sharp
#Date: April 2, 2025
#Assignment #: 7
#By submitting this assignment, I declare that the source code contained in this assignment was written #solely by me, unless specifically provided in the assignment. I attest that no part of this assignment, #in whole or in part, was directly created by Generative AI, unless explicitly stated in the assignment #instructions, nor obtained from a subscription service. I understand that copying any source code, #in whole or in part, unless specifically provided in the assignment, constitutes cheating, and that #I will receive a zero on this project if I am found in violation of this policy.

import tkinter as tk
from tkinter import ttk, messagebox
import random

class applicationFrames(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        applicationFrame(parent).grid(column=0, row=0)

        ttk.Button(parent, text="Exit", command=parent.destroy).grid(column=1, row=2, sticky=tk.E, padx=15, pady=10)

class applicationFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.message = ""

        self.length = tk.StringVar()
        self.passcode = tk.StringVar()

        self.initComponents()

    def initComponents(self):
        ttk.Label(self, text="Password Length:").grid(column=0, row=0, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.length).grid(column=1, row=0)

        ttk.Label(self, text="Generated Passcode:").grid(column=0, row=1, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.passcode).grid(column=1, row=1)

        self.makeButtons()

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

    def makeButtons(self):
        buttonFrame = ttk.Frame(self)

        buttonFrame.grid(column=0, row=3, columnspan=2, sticky=tk.E)

        ttk.Button(buttonFrame, text="Clear", command=self.clear).grid(column=0, row=0, padx=5)
        ttk.Button(buttonFrame, text="Generate", command=self.generate).grid(column=1, row=0)

    def clear(self):
        self.length.set("")
        self.passcode.set("")
    
    def generate(self):
        self.message = ""

        length = int(self.length.get())
        minLength = 10 ** (length - 1)
        maxLength = 10 ** length
        passcode = random.randint(minLength, maxLength - 1)

        self.passcode.set(passcode)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Passcode Generator")
    applicationFrames(root)
    root.mainloop()