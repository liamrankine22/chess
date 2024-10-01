import tkinter
from tkinter import *

root = Tk()
root.title("Chess")

length = 8
width = 8

board = [[0 for x in range(length)] for y in range(width)]

for x in range(0, length):
    for y in range(0, width):
        if (y % 2 == 1) & (x % 2 == 0) | (x % 2 == 1) & (y % 2 == 0):
            tile = tkinter.Button(root, width=13 , height=5, state=tkinter.DISABLED, bg="#5c915d")

        else:
            tile = tkinter.Button(root, width=13, height=5, state=tkinter.DISABLED, bg="#ddebc3")

        tile.grid(row=x, column=y)

root.mainloop()