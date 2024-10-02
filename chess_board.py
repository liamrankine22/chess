import tkinter
from tkinter import *
from PIL import Image, ImageTk

class Board:

    def __init__(self):
        self.board = [[0 for x in range(0, 8)] for y in range(0, 8)]
        self.pieces_placement = [["" for x in range(0, 8)] for y in range(0, 8)]

        # Black Bishop Image
        self.b_bishop_image = Image.open("Pieces/b_bishop_png_128px.png")
        self.b_bishop = self.resize_image(self.b_bishop_image, 70, 60)

        # Black King Image
        self.b_king_image = Image.open("Pieces/b_king_png_128px.png")
        self.b_king = self.resize_image(self.b_king_image, 70, 60)

        # Black Knight Image
        self.b_knight_image = Image.open("Pieces/b_knight_png_128px.png")
        self.b_knight = self.resize_image(self.b_knight_image, 70, 60)

        # Black Pawn Image
        self.b_pawn_image = Image.open("Pieces/b_pawn_png_128px.png")
        self.b_pawn = self.resize_image(self.b_pawn_image, 70, 60)

        # Black Queen Image
        self.b_queen_image = Image.open("Pieces/b_queen_png_128px.png")
        self.b_queen = self.resize_image(self.b_queen_image, 70, 60)

        #Black Rook Image
        self.b_rook_image = Image.open("Pieces/b_rook_png_128px.png")
        self.b_rook = self.resize_image(self.b_rook_image, 70, 60)

        #White Bishop Image
        self.w_bishop_image = Image.open("Pieces/w_bishop_png_128px.png")
        self.w_bishop = self.resize_image(self.w_bishop_image, 70, 60)

        # White King Image
        self.w_king_image = Image.open("Pieces/w_king_png_128px.png")
        self.w_king = self.resize_image(self.w_king_image, 70, 60)

        # White Knight Image
        self.w_knight_image = Image.open("Pieces/w_knight_png_128px.png")
        self.w_knight = self.resize_image(self.w_knight_image, 70, 60)

        # White Pawn Image
        self.w_pawn_image = Image.open("Pieces/w_pawn_png_128px.png")
        self.w_pawn = self.resize_image(self.w_pawn_image, 70, 60)

        # White Queen Image
        self.w_queen_image = Image.open("Pieces/w_queen_png_128px.png")
        self.w_queen = self.resize_image(self.w_queen_image, 70, 60)

        # White Rook Image
        self.w_rook_image = Image.open("Pieces/w_rook_png_128px.png")
        self.w_rook = self.resize_image(self.w_rook_image, 70, 60)

    def resize_image(self, image, width, length):
        image = image.resize((width, length), Image.LANCZOS)
        return ImageTk.PhotoImage(image)

    def make_board(self):
        try:
            for x in range(0, 8):
                for y in range(0, 8):
                    if (y % 2 == 1) & (x % 2 == 0) | (x % 2 == 1) & (y % 2 == 0):
                        tile = tkinter.Button(root, bg="#5c915d")

                    else:
                        tile = tkinter.Button(root, bg="#ddebc3")

                    tile.place(x= 90 * y,y= 80 * x, width= 90, height= 80)

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
        i = 0

        for t in first_row:
            if i == 0 or i == 7:
                t.config(image=self.b_rook, compound='center')

            elif i == 1 or i == 6:
                t.config(image=self.b_knight, compound='center')

            elif i == 2 or i == 5:
                t.config(image=self.b_bishop, compound='center')

            elif i == 3:
                t.config(image=self.b_queen, compound='center')

            else:
                t.config(image=self.b_king, compound='center')

            i += 1
        i = 0

        for t in second_row:
            t.config(image=self.b_pawn, compound='center')
            self.pieces_placement[1][i] = 'p'
            i += 1
        i = 0

        for t in second_last_row:
            t.config(image=self.w_pawn, compound='center')
            self.pieces_placement[6][i] = 'p'
            i += 1
        i = 0

        for t in last_row:
            if i == 0 or i == 7:
                t.config(image=self.w_rook, compound='center')

            elif i == 1 or i == 6:
                t.config(image=self.w_knight, compound='center')

            elif i == 2 or i == 5:
                t.config(image=self.w_bishop, compound='center')

            elif i == 3:
                t.config(image=self.w_queen, compound='center')

            else:
                t.config(image=self.w_king, compound='center')

            i += 1
        i = 0

root = Tk()
root.title("Chess")
root.geometry("720x640")
board = Board()
board.make_board()
board.place_pieces()

root.mainloop()