import tkinter
from tkinter import *
from PIL import Image, ImageTk
from selected_pieces import *


class CreateBoard:
    """
    Class for the creating the visuals of the chess board along with
    placing the pieces and recording their starting positions

    Attributes:
        board (tkinter button): 2d array of tkinter buttons used for interacting with the board
        pieces_placement (str): 2d array of strings used for checking the location of each piece on the board
        current_piece (tuple): tuple containing the coordinates of the currently clicked piece
        b_bishop (image): Image containing the black bishop image
        b_king (image): Image containing the black king image
        b_knight (image): Image containing the black knight image
        b_pawn (image): Image containing the black pawn image
        b_queen (image): Image containing the black queen image
        b_rook (image): Image containing the black rook image
        w_bishop (image): Image containing the white bishop image
        w_king (image): Image containing the white king image
        w_knight (image): Image containing the white knight image
        w_pawn (image): Image containing the white pawn image
        w_queen (image): Image containing the white queen image
        w_rook (image): Image containing the white rook image

    Methods:
        create_image(path: str, width: int, length: int) --> ImageTk
            Opens and resizes images
        clicked_piece(row: int, length: int) --> tuple
            Stores the location of the clicked piece
        make_board() --> None
            Creates the board and stores the button as tiles in a 2d array
        place_pieces() --> None
            Places the pieces on the board by putting images on the starting tiles and storing
            their locations in a 2d array
        place_pieces_helper(row_list: tiles, row: int, i: int, colour: str) --> None
            Helper function for the place_pieces method that places the pieces on the back rows
    """

    def __init__(self):
        """
        Initializer for CreateBoard variables
        """
        self.board = [[0 for x in range(0, 8)] for y in range(0, 8)]
        self.pieces_placement = [["" for x in range(0, 8)] for y in range(0, 8)]

        self.current_piece = None

        self.b_bishop = self.create_image("Pieces/b_bishop_png_128px.png", 70, 60) # Black Bishop Image
        self.b_king = self.create_image("Pieces/b_king_png_128px.png", 70, 60) # Black King Image
        self.b_knight = self.create_image("Pieces/b_knight_png_128px.png", 70, 60) # Black Knight Image
        self.b_pawn = self.create_image("Pieces/b_pawn_png_128px.png", 70, 60) # Black Pawn Image
        self.b_queen = self.create_image("Pieces/b_queen_png_128px.png", 70, 60) # Black Queen Image
        self.b_rook = self.create_image("Pieces/b_rook_png_128px.png", 70, 60) # Black Rook Image

        self.w_bishop = self.create_image("Pieces/w_bishop_png_128px.png", 70, 60) # White Bishop Image
        self.w_king = self.create_image("Pieces/w_king_png_128px.png", 70, 60) # White King Image
        self.w_knight = self.create_image("Pieces/w_knight_png_128px.png", 70, 60) # White Knight Image
        self.w_pawn = self.create_image("Pieces/w_pawn_png_128px.png", 70, 60) # White Pawn Image
        self.w_queen = self.create_image("Pieces/w_queen_png_128px.png", 70, 60) # White Queen Image
        self.w_rook = self.create_image( "Pieces/w_rook_png_128px.png", 70, 60) # White Rook Image

    def create_image(self, path: str, width: int, length: int):
        """
        Loading and Resizing Images

        :param path: Path to image file
        :param width: Desired width in pixels of image
        :param length: Desired length in pixels of image

        :return: The resized image
        """
        path = Image.open(path)
        path = path.resize((width, length), Image.LANCZOS)
        return ImageTk.PhotoImage(path)

    def clicked_piece(self, row: int, column: int):
        """
        Saves the location of the clicked piece

        :param row: the location of the piece on its row
        :param column: the location of the piece on its column

        :return: the saved position of the current piece as a tuple
        """
        self.current_piece = (row, column)

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

    def place_pieces_helper(self, row_list, row, i, colour:str):
        """
        Helper function for the place_pieces method. Places the back rows of each side

        :param row_list: the list of tiles on the given row
        :param row: the row for the tiles to be placed on
        :param i: iterated number to be used for the column
        :param colour: the string value of the colour

        :return: None
        """
        for tile in row_list:
            if i == 0 or i == 7:
                if colour == 'b':
                    tile.config(image=self.b_rook, compound='center', command=lambda column=i: self.clicked_piece(row, column))
                    self.pieces_placement[row][i] = f'{colour}r'
                else:
                    tile.config(image=self.w_rook, compound='center', command=lambda column=i: self.clicked_piece(row, column))
                    self.pieces_placement[row][i] = f'{colour}r'

            elif i == 1 or i == 6:
                if colour == 'b':
                    tile.config(image=self.b_knight, compound='center', command=lambda column=i: self.clicked_piece(row, column))
                    self.pieces_placement[row][i] = f'{colour}n'
                else:
                    tile.config(image=self.w_knight, compound='center', command=lambda column=i: self.clicked_piece(row, column))
                    self.pieces_placement[row][i] = f'{colour}n'

            elif i == 2 or i == 5:
                if colour == 'b':
                    tile.config(image=self.b_bishop, compound='center', command=lambda column=i: self.clicked_piece(row, column))
                    self.pieces_placement[row][i] = f'{colour}b'
                else:
                    tile.config(image=self.w_bishop, compound='center', command=lambda column=i: self.clicked_piece(row, column))
                    self.pieces_placement[row][i] = f'{colour}b'

            elif i == 3:
                if colour == 'b':
                    tile.config(image=self.b_queen, compound='center', command=lambda column=i: self.clicked_piece(row, column))
                    self.pieces_placement[row][i] = f'{colour}q'
                else:
                    tile.config(image=self.w_queen, compound='center', command=lambda column=i: self.clicked_piece(row, column))
                    self.pieces_placement[row][i] = f'{colour}q'

            else:
                if colour == 'b':
                    tile.config(image=self.b_king, compound='center', command=lambda x=i: self.clicked_piece(0, x))
                    self.pieces_placement[row][i] = f'{colour}k'
                else:
                    tile.config(image=self.w_king, compound='center', command=lambda column=i: self.clicked_piece(row, column))
                    self.pieces_placement[row][i] = f'{colour}k'
            i += 1

    def place_pieces(self):
        """
        Places pieces on the chessboard by placing images on their corresponding starting tiles
        in traditional chess. Stores the tiles with placed images into a 2d array containing strings.
        The first character in the string stores the colour of the piece and the second
        stores the type of piece (e.g, white bishop = 'br')

        :return: None
        """
        first_row = self.board[0]
        second_row = self.board[1]
        second_last_row = self.board[6]
        last_row = self.board[7]
        i = 0
        self.place_pieces_helper(first_row, 0, i, 'b')
        i = 0

        for tile in second_row:
            tile.config(image=self.b_pawn, compound='center', command= lambda x=i : self.clicked_piece(1, x))
            self.pieces_placement[1][i] = 'bp'
            i += 1
        i = 0

        for tile in second_last_row:
            tile.config(image=self.w_pawn, compound='center', command= lambda x=i : self.clicked_piece(6, x))
            self.pieces_placement[6][i] = 'wp'
            i += 1
        i = 0

        self.place_pieces_helper(last_row, 7, i, 'w')
        i = 0

        for num in range (2,6):
            for i in range(8):
                tile = self.board[num][i]
                tile.config(command=lambda x = num, y = i: self.clicked_piece(x, y))
        i = 0

class PlayChess(CreateBoard):
    def __init__(self):
        super().__init__()
        self.make_board() #creates board
        self.place_pieces() #places pieces on board
        self.moveable_spots = SelectedPieces()
        self.selected_piece = None
        self.selected_piece_x = None
        self.selected_piece_y = None


    def clicked_piece(self, x, y):
        super(PlayChess, self).clicked_piece(x, y)
        x_pos, y_pos = self.current_piece
        #print(f"{x_pos}, {y_pos}")
        piece = self.pieces_placement[x_pos][y_pos]
        #print(piece)
        #print(f"Checking piece at {x_pos}, {y_pos}: {piece}")

        if piece == '':
            if self.selected_piece is not None:
                move_to_space = self.moveable_spots.iterate(self.board[x][y])
                if move_to_space is not None:
                    if (y % 2 == 1) & (x % 2 == 0) | (x % 2 == 1) & (y % 2 == 0):
                        print(move_to_space.data)
                        image = self.selected_piece.cget("image")
                        command = self.selected_piece.cget("command")
                        move_to_space.data.config(bg="#5c915d", image=image)
                        print("Clearing image from selected piece:", self.selected_piece)
                        self.board[self.selected_piece_x][self.selected_piece_y].config(image=None)
                        print("sucessfully cleared image")
                        self.selected_piece=None
                    else:
                        print(move_to_space.data)
                        image = self.selected_piece.cget("image")
                        command = self.selected_piece.cget("command")
                        move_to_space.data.config(bg="#ddebc3", image=image)
                        print("Clearing image from selected piece:", self.selected_piece)
                        self.board[self.selected_piece_x][self.selected_piece_y].config(image=None)
                        print("sucessfully cleared image")
                        self.selected_piece = None

        elif piece[1] == 'r': #rook
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
            self.selected_piece = self.board[x][y]
            self.selected_piece_x = x
            self.selected_piece_y = y
            print(self.selected_piece)
            if piece[0] == 'b':
                if x_pos + 1 < 8:
                    tile = self.board[x_pos + 1][y_pos]
                    tile.config(bg="#d11d3e")
                    self.moveable_spots.add_selected_piece(tile)
                if x_pos == 1:
                    tile = self.board[x_pos + 2][y_pos]
                    tile.config(bg="#d11d3e")
                    self.moveable_spots.add_selected_piece(tile)
            elif piece[0] == 'w':
                if x_pos - 1 > 0:
                    tile = self.board[x_pos - 1][y_pos]
                    tile.config(bg="#d11d3e")
                    self.moveable_spots.add_selected_piece(tile)
                if x_pos == 6:
                    tile = self.board[x_pos - 2][y_pos]
                    tile.config(bg="#d11d3e")
                    self.moveable_spots.add_selected_piece(tile)

root = Tk()
root.title("Chess")
root.geometry("720x640")

board = PlayChess()

root.mainloop()