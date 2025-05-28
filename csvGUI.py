import tkinter
from tkinter import StringVar, scrolledtext

import csvLauncherAndCommands

mainWindow = tkinter.Tk()
mainWindow.title("CSV File Analyzer")
mainWindow.geometry("500x500")

radioButtonOptionControl = StringVar(value="A")

inputField = tkinter.Entry(mainWindow, state=tkinter.DISABLED)
inputField.pack(side=tkinter.TOP, padx=10, pady=50)
inputField.place(x=131, y=25, width=155, height=23)

browseFilesButton = tkinter.Button(mainWindow, text="Browse Files", command=csvLauncherAndCommands.browseFilesCommand)
browseFilesButton.pack(side=tkinter.TOP, padx=10, pady=50)
browseFilesButton.place(x=300, y=25)

radioButtonHeadersOption = tkinter.Radiobutton(mainWindow, text="Fieldnames", variable=radioButtonOptionControl, value="A")
radioButtonHeadersOption.pack(side=tkinter.TOP, padx=5, pady=100)
radioButtonHeadersOption.place(x=103, y=59)

radioButtonColumnsOption = tkinter.Radiobutton(mainWindow, text="Columns", variable=radioButtonOptionControl, value="B")
radioButtonColumnsOption.pack(side=tkinter.TOP, padx=5, pady=100)
radioButtonColumnsOption.place(x=192, y=59)

radioButtonRowsOption = tkinter.Radiobutton(mainWindow, text="Rows", variable=radioButtonOptionControl, value="C")
radioButtonRowsOption.pack(side=tkinter.TOP, padx=5, pady=100)
radioButtonRowsOption.place(x=272, y=59)

radioButtonAllOptions = tkinter.Radiobutton(mainWindow, text="All", variable=radioButtonOptionControl, value="D")
radioButtonAllOptions.pack(side=tkinter.TOP, padx=5, pady=100)
radioButtonAllOptions.place(x=332, y=59)

fieldNameName = tkinter.Label(mainWindow, text="Column Name:")
fieldNameName.pack(side=tkinter.TOP, padx=10, pady=50)
fieldNameName.place(x=75, y=125, width=155, height=23)

inputField2 = tkinter.Entry(mainWindow)
inputField2.pack(side=tkinter.TOP, padx=10, pady=50)
inputField2.place(x=200, y=125, width=155, height=23)

fieldNameNameName = tkinter.Label(mainWindow, text="Row Name:")
fieldNameNameName.pack(side=tkinter.TOP, padx=10, pady=50)
fieldNameNameName.place(x=85, y=92, width=155, height=23)

inputField3 = tkinter.Entry(mainWindow)
inputField3.pack(side=tkinter.TOP, padx=10, pady=50)
inputField3.place(x=200, y=92, width=155, height=23)


button = tkinter.Button(mainWindow, text="Get", command=csvLauncherAndCommands.processCSV)
button.pack(side=tkinter.BOTTOM, padx=10, pady=50)
button.place(x=200, y=160)

button2 = tkinter.Button(mainWindow, text="Clear", command=csvLauncherAndCommands.clearFilePathInputFieldCommand)
button2.pack(side=tkinter.BOTTOM, padx=10, pady=50)
button2.place(x=260, y=160)

outputArea = scrolledtext.ScrolledText(mainWindow, wrap=tkinter.WORD, width=58, height=18, state=tkinter.DISABLED)
outputArea.pack(side=tkinter.BOTTOM)
outputArea.place(x=10, y=200)

mainWindow.mainloop()