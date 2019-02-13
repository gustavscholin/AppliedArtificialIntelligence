import copy
from enum import Enum
import numpy as np

class Turn(Enum):
    WHITE = 0
    BLACK = 1


# Enum representing the pieces on the board
class Piece(Enum):
    NONE = 0
    WHITE = 1
    BLACK = 2

class Board:

    # Init the board with start state
    def __init__(self):
        self.board = np.zeros((8,8))
        self.board[3, 3] = Piece.WHITE.value
        self.board[4, 4] = Piece.WHITE.value
        self.board[3, 4] = Piece.BLACK.value
        self.board[4, 3] = Piece.BLACK.value
        self.empty_adj = []

    # Get all the valid moves for the current player
    def validMoves(self, turn):

        # Assume white turn
        opponent_pieces = self.blacks
        # Check for black turn
        if turn == Turn.BLACK:
            opponent_pieces = self.whites

        # Find all open places adj to opponent tiles for potential moves
        potential_moves = []
        for i in range(0,len(opponent_pieces)):
            curr_piece = opponent_pieces[i]


    def getEmptyAdj(self, coords):
        # TODO
        pass

    def getScore(self, turn):
        score = 0
        for slot in np.nditer(self.board):
            if turn.value == slot:
                score = score + 1
        return score

    def update(self, move, turn):
        self.board[move[0],move[1]] = Piece[turn.name].value

    def __str__(self):
        return str(self.board)





