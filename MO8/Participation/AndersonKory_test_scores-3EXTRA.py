import tkinter as tk
from tkinter import ttk, messagebox

class testScoresFrames(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        testScoresFrame(parent).grid(row=0, column=0)

        ttk.Button(parent, text="Exit", command=parent.destroy).grid(column=1, row =2, sticky=tk.E, padx=15, pady=10)

class testScoresFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.message = ""

        self.testScore = [tk.StringVar()]
        self.length = tk.StringVar()
        self.avgScore = tk.StringVar()
        self.minScore = tk.StringVar()
        self.maxScore = tk.StringVar()
        self.medianScore = tk.StringVar()
        self.counter =tk.StringVar()

        self.initComponents()
    
    def clear(self):
        self.testScore.set("")
        self.length.set("")
        self.avgScore.set("")
        self.minScore.set("")
        self.maxScore.set("")
        self.medianScore.set("")
        self.counter.set("")
    
    def makeTestScore(self):
        counter = self.counter.get()
        if counter == "":
            counter = 1
        else:
            counter = int(counter)
            counter += 1
        self.testScore.append(tk.StringVar())
        ttk.Label(self, text="Test Score:").grid(column=0, row=counter, sticky=tk.E, padx=5, pady=3)
        ttk.Entry(self, width=25, textvariable=self.testScore[counter]).grid(column=1, row=counter, padx=5, pady=3)

        counter = str(counter)
        self.counter.set(f"{counter}")

    def initComponents(self):
        ttk.Label(self, text="Test Score:").grid(column=0, row=0, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.testScore[0]).grid(column=1, row=0)

        ttk.Label(self, text="Amount of Scores Entered:").grid(column=2, row=0, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.length).grid(column=3, row=0)

        ttk.Label(self, text="Average Test Score:").grid(column=2, row=1, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.avgScore).grid(column=3, row=1)

        ttk.Label(self, text="Minimum Test Score:").grid(column=2, row=2, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.minScore).grid(column=3, row=2)

        ttk.Label(self, text="Maximum Test Score:").grid(column=2, row=3, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.maxScore).grid(column=3, row=3)

        ttk.Label(self, text="Median Test Score(s):").grid(column=2, row=4, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.medianScore).grid(column=3, row=4)

        self.makeButtons()

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)
    
    def makeButtons(self):
        buttonFrame = ttk.Frame(self)

        buttonFrame.grid(column=2, row=5, columnspan=2, sticky=tk.E)

        ttk.Button(buttonFrame, text="Clear", command=self.clear).grid(column=0, row=0, padx=5)
        ttk.Button(buttonFrame, text="Calculate", command=self.calculate).grid(column=1, row=0, padx=5)
        ttk.Button(buttonFrame, text="Add Test Score", command=self.makeTestScore).grid(column=2, row=0)
    
    def getInt(self, val, fieldName):
        try:
            return int(val)
        except ValueError:
            self.message += f"{fieldName} must be a valid integer"
    
    def calculate(self):
        self.message = ""

        testScores = []
        counter = int(self.counter.get())
        for i in range(0, counter + 1):
            testScores.append(self.getInt(self.testScore[i].get(), "Test Score"))

        if self.message == "":
            length = len(testScores)
            testScores.sort()
            totalScore = 0
            medianScore = []
            for i in testScores:
                totalScore += i
            avgScore = totalScore / length
            minScore = min(testScores)
            maxScore = max(testScores)
            medianIndex = length / 2
            if medianIndex % 2 != 0:
                medianIndex = int(medianIndex - .5)
                medianScore.append(testScores[medianIndex])
            else:
                medianIndex1 = int(medianIndex - .5)
                medianIndex2 = int(medianIndex + .5)
                medianScore.append(testScores[medianIndex1])
                medianScore.append(testScores[medianIndex2])
            self.length.set(length)
            self.avgScore.set(avgScore)
            self.minScore.set(minScore)
            self.maxScore.set(maxScore)
            self.medianScore.set(medianScore)
        else:
            messagebox.showerror("Error", self.message)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Test Scores App")
    testScoresFrames(root)
    root.mainloop()            