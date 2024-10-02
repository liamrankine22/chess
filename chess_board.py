import tkinter
from tkinter import *

class Board:

    def __init__(self):
        self.row = 8
        self.column = 8
        self.board = [[0 for x in range(self.row)] for y in range(self.column)]
        self.pieces_placement = [[0 for x in range(self.row)] for y in range(self.column)]

    def make_board(self):
        try:
            for x in range(0, self.row):
                for y in range(0, self.column):
                    if (y % 2 == 1) & (x % 2 == 0) | (x % 2 == 1) & (y % 2 == 0):
                        tile = tkinter.Button(root, width=13 , height=5, state=tkinter.DISABLED, bg="#5c915d")

                    else:
                        tile = tkinter.Button(root, width=13, height=5, state=tkinter.DISABLED, bg="#ddebc3")

                    tile.grid(row=x, column=y)

                    self.board[x][y] = tile
        except Exception as e:
            print("Error making board")
            return -1

        return 0

    def place_pieces(self):
        first_row = self.board[0]
        second_row = self.board[1]
        second_last_row = self.board[6]
        last_row = self.board[7]

        for t in first_row:
            print("Sigma")

        for t in second_row:
            print("sigma 2")

        for t in second_last_row:
            print("sigma 3")

        for t in last_row:
            print("sigma 4")

root = Tk()
root.title("Chess")
board = Board()
board.make_board()

root.mainloop()