# Name: Rusho Binnabi
# Date: 6/6/2025
# Project: CSV - Launcher and Commands
# Contact Information: RushoBinnabi123@yahoo.com

import csv
import tkinter as tk
from tkinter.filedialog import askopenfilename

import csvGUI

# this csvLauncherAndCommands file has all the code needed for the application to function.

filePath = ""
fieldName = []

# this browseFilesCommand() function gets the csv files that will be used and processed by the application
# when the appropriate button is clicked.

def browseFilesCommand():
    tk.Tk().withdraw()
    fn = askopenfilename()
    csvGUI.inputField.config(state=tk.NORMAL)
    csvGUI.inputField.insert(tk.END, fn)
    csvGUI.inputField.config(state=tk.DISABLED)

# this clearFilePathInputFieldCommand() function will clear the application screen when the appropriate button is clicked.

def clearFilePathInputFieldCommand():
    csvGUI.outputArea.config(state=tk.NORMAL)
    csvGUI.inputField.config(state=tk.NORMAL)
    csvGUI.outputArea.delete(1.0, tk.END)
    csvGUI.inputField.delete(0, tk.END)
    csvGUI.outputArea.config(state=tk.DISABLED)
    csvGUI.inputField.config(state=tk.DISABLED)
    csvGUI.inputField2.config(state=tk.NORMAL)
    csvGUI.inputField3.config(state=tk.NORMAL)
    csvGUI.radioButtonHeadersOption.select()

# this processCSV() will process the csv file and display it on the GUI when the appropriate button is clicked.

def processCSV():
    filePath = csvGUI.inputField.get()
    if csvGUI.radioButtonOptionControl.get() == "A":
        csvGUI.outputArea.config(state=tk.NORMAL)
        with open(filePath, "r", encoding="utf-8") as csvFile:
            fieldNames = csv.DictReader(csvFile)
            csvGUI.outputArea.insert(tk.END, fieldNames.fieldnames)
        csvGUI.outputArea.config(state=tk.DISABLED)
    elif csvGUI.radioButtonOptionControl.get() == "B":
        csvGUI.outputArea.config(state=tk.NORMAL)
        with open(filePath, "r", encoding="utf-8") as csvFile:
            file = csv.DictReader(csvFile)
            column = csvGUI.inputField2.get()
            if column in file.fieldnames:
                for readRow in file:
                    #print(readRow[column]) # used for debugging.
                    csvGUI.outputArea.insert(tk.END, readRow[column] + "\n")
        csvGUI.outputArea.config(state=tk.DISABLED)
    elif csvGUI.radioButtonOptionControl.get() == "C":
        csvGUI.outputArea.config(state=tk.NORMAL)
        with open(filePath, "r", encoding="utf-8") as csvFile:
            file = csv.reader(csvFile)
            row = csvGUI.inputField3.get()
            for readRow in file:
                if row in readRow:
                    #print(readRow) # used for debugging.
                    csvGUI.outputArea.insert(tk.END, readRow)
    elif csvGUI.radioButtonOptionControl.get() == "D":
        csvGUI.inputField2.config(state=tk.DISABLED)
        with open(filePath, "r", encoding="utf-8") as csvFile:
            csvGUI.outputArea.config(state=tk.NORMAL)
            reader = csv.DictReader(csvFile)
            for everything in reader:
                csvGUI.outputArea.insert(tk.END, str(everything) + str("\n"))
            csvGUI.outputArea.config(state=tk.DISABLED)