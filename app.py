"""
GUI made using tkinter module in python

"""

import tkinter as tk
from tkinter import Text 


# initialize the root
root = tk.Tk()

# initialize the canvas
canvas = tk.Canvas(root, height= 700, width= 700, bg="#263D42")
canvas.pack()

# show the window of the gui
root.mainloop()