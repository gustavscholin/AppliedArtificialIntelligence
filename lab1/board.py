from enum import Enum
import numpy as np

class Piece(Enum):
    NONE = 0
    WHITE = 1
    BLACK = 2

class Board:

    def __init__(self):
        self.board = np.zeros((8,8))
        self.board[3, 3] = Piece.WHITE
        self.board[4, 4] = Piece.WHITE
        self.board[3, 4] = Piece.BLACK
        self.board[4, 3] = Piece.BLACK


    def validMoves(self, turn):
        pass