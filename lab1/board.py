from enum import Enum
import numpy as np

from lab1.game import Turn


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
        self.blacks = [(3,4), (4,3)]
        self.whites = [(3,3), (4,4)]


    def validMoves(self, turn):
        if turn == Turn.BLACK:
            occupied = self.whites
        else:
            occupied = self.blacks

