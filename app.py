"""
GUI made using tkinter module in python

"""

import tkinter as tk
from tkinter import Text 


# initialize the root
root = tk.Tk()

# initialize the canvas
canvas = tk.Canvas(root, width= 1000, height= 1000, bg="#263D42")
canvas.pack()


# initialize frame
frame = tk.Frame(root, bg = "white")
frame.place(relwidth= 0.8 , relheight= 0.8 , relx= 0.1, rely= 0.1)


# show the window of the gui
root.mainloop()