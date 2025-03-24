#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk, messagebox
import locale

from calculator import calculation

class calculatorFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.parent = parent
        self.calculation = calculation()
        self.message = ""

        locale.setlocale(locale.LC_ALL, 'en_US')

        self.diameter = tk.StringVar()
        self.circumference = tk.StringVar()

        self.initCompenents()

    def clear(self):
        self.diameter.set("")
        self.circumference.set("")

    def initCompenents(self):
        ttk.Label(self, text="Diameter").grid(column=0, row=0, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.diameter).grid(column=1, row=1)

        ttk.Label(self, text="Circumference").grid(column=0, row=1, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.circumference).grid(column=1, row=1)

        self.makeButtons()

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

    def makeButtons(self):
        buttonFrame = ttk.Frame(self)

        buttonFrame.grid(column=0, row=3, columnspan=2, sticky=tk.E)

        ttk.Button(buttonFrame, text="Clear", command=self.clear).grid(column=0, row=0, padx=5)
        ttk.Button(buttonFrame, text="Calculate", command=self.calculate).grid(column=1, row=0)

    def getFloat(self, val, fieldName):
        try:
            return float(val)
        except ValueError:
            self.message += f"{fieldName} must be a valid number"
    
    def calculate(self):
        self.message = ""

        self.calculation.diameter = self.getFloat(self.diameter.get(), "Diameter")
        self.calculation.circumference = self.getFloat(self.circumference.get(), "Circumference")

        if self.message == "":
            self.final.set(self.calculation.calculate(), grouping=True)
        else:
            messagebox.showerror("Error", self.message)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Circle Calculator")
    calculatorFrame(root)
    root.mainloop()