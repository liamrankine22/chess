import tkinter
from tkinter import *
from PIL import Image, ImageTk


class CreateBoard:
    def __init__(self):
        self.board = [[0 for x in range(0, 8)] for y in range(0, 8)]
        self.pieces_placement = [["" for x in range(0, 8)] for y in range(0, 8)]

        self.current_piece = None

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

        # Black Rook Image
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

    def clicked_piece(self, x, y):
        self.current_piece = (x,y)

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
            print("Error making board.")
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
                t.config(image=self.b_rook, compound='center', command= lambda x=i : self.clicked_piece(0, x))
                self.pieces_placement[0][i] = 'br'

            elif i == 1 or i == 6:
                t.config(image=self.b_knight, compound='center', command= lambda x=i : self.clicked_piece(0, x))
                self.pieces_placement[0][i] = 'bn'

            elif i == 2 or i == 5:
                t.config(image=self.b_bishop, compound='center', command= lambda x=i : self.clicked_piece(0, x))
                self.pieces_placement[0][i] = 'bb'

            elif i == 3:
                t.config(image=self.b_queen, compound='center', command= lambda x=i : self.clicked_piece(0, x))
                self.pieces_placement[0][i] = 'bq'

            else:
                t.config(image=self.b_king, compound='center', command= lambda x=i : self.clicked_piece(0, x))
                self.pieces_placement[0][i] = 'bk'

            i += 1
        i = 0

        for t in second_row:
            t.config(image=self.b_pawn, compound='center', command= lambda x=i : self.clicked_piece(1, x))
            self.pieces_placement[1][i] = 'bp'
            i += 1
        i = 0

        for t in second_last_row:
            t.config(image=self.w_pawn, compound='center', command= lambda x=i : self.clicked_piece(6, x))
            self.pieces_placement[6][i] = 'wp'
            i += 1
        i = 0

        for t in last_row:
            if i == 0 or i == 7:
                t.config(image=self.w_rook, compound='center', command= lambda x=i : self.clicked_piece(7, x))
                self.pieces_placement[7][i] = 'wr'

            elif i == 1 or i == 6:
                t.config(image=self.w_knight, compound='center', command= lambda x=i : self.clicked_piece(7, x))
                self.pieces_placement[7][i] = 'wn'

            elif i == 2 or i == 5:
                t.config(image=self.w_bishop, compound='center', command= lambda x=i : self.clicked_piece(7, x))
                self.pieces_placement[7][i] = 'wb'

            elif i == 3:
                t.config(image=self.w_queen, compound='center', command= lambda x=i : self.clicked_piece(7, x))
                self.pieces_placement[7][i] = 'wq'

            else:
                t.config(image=self.w_king, compound='center', command= lambda x=i : self.clicked_piece(7, x))
                self.pieces_placement[7][i] = 'wk'
            i += 1
        i = 0

class PlayChess(CreateBoard):
    def __init__(self):
        super().__init__()
        self.make_board() #creates board
        self.place_pieces() #places pieces on board

    def clicked_piece(self, x, y):
        super(PlayChess, self).clicked_piece(x, y)
        x_pos, y_pos = self.current_piece
        print(f"{x_pos}, {y_pos}")
        piece = self.pieces_placement[x_pos][y_pos]
        print(piece)

        if piece[1] == 'r': #rook
            print("r")

        elif piece[1] == 'n': #knight
            print("n")

        elif piece[1] == 'b': #bishop
            print("b")

        elif piece[1] == 'q': #queen
            print("q")

        elif piece[1] == 'k': #king
            print("k")

        elif piece[1] == 'p': #pawn
            if piece[0] == 'b':
                if x_pos + 1 < 8:
                    tile = self.board[x_pos + 1][y_pos]
                    tile.config(bg="#d11d3e")
            elif piece[0] == 'w':
                if x_pos - 1 > 0:
                    tile = self.board[x_pos - 1][y_pos]
                    tile.config(bg="#d11d3e")

root = Tk()
root.title("Chess")
root.geometry("720x640")

board = PlayChess()

root.mainloop()