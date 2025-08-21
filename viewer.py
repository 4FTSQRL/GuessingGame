"""
Author: 4FTSQRL

Usage: python viewer.py

Description: Viewer for the game. Here is where people can interact with the game and submit their guesses.
"""

# Import Statements
import test
#Tkinter
from tkinter import *
from tkinter import ttk

# Create the GUI
root = Tk()
# Add a title
root.title("Guess the Price")

# Frames
frame = ttk.Frame(root)
frame.grid(row=0,column=0,columnspan=2)

# Get the keys and clean it up by putting it in a list
keys = (test.guesses()).keys()
names = []
i = 0
for k in keys:
    names.insert(i, k)
    i += 1
    
# Combo box
nameCmbx = ttk.Combobox(frame, values=names)
nameCmbx.set("Select your name")
nameCmbx.grid(padx=100, pady=10)

# Calling the main loop for Tk
root.mainloop()