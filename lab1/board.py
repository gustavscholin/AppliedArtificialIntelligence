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
        self.empty_adj = [(2,2), (2,3), (2,4), (2,5), (3,2), (3,5), (4,2), (4,5),
                          (5,2), (5,3), (5,4), (5,5)]

    # Get all the valid moves for the current player
    def validMoves(self, turn):
        valid_moves = []
        # Check every empty square adj to a piece
        for sqr in self.empty_adj:
            if self.isValidMove(turn, sqr):
                valid_moves.append(sqr)
        return valid_moves

    # Check a given square is a valid move for a specific player
    def isValidMove(self, turn, move):
        isValid = False
        for sqr in self.getFilledAdj(move):
            dir = (sqr[0] - move[0], sqr[1] - move[1])
            isValid = self.wouldBeConvertedLine(turn, move, dir)
            if isValid:
                break
        return isValid

    # Check if a certain line would be converted if a player where to make this move
    def wouldBeConvertedLine(self, turn, move, dir):
        turnPiece = Piece.WHITE.value if turn == Turn.WHITE else Piece.BLACK.value
        opponentPiece = Piece.BLACK.value if turn == Turn.WHITE else Piece.WHITE.value
        foundOpponent = False
        converted = False
        i = move[0]
        j = move[1]
        while not converted:
            i += dir[0]  # Current square to consider
            j += dir[1]
            if i < 0 or i > 7 or j < 0 or j > 7 or self.board[i, j] == Piece.NONE.value:
                break
            if self.board[i, j] == opponentPiece:
                foundOpponent = True
            elif self.board[i, j] == turnPiece and foundOpponent:
                converted = True
        return converted

    # Return a list of all the empty adjacent squares to the given square
    def getEmptyAdj(self, coords):
        return self.getAdj(coords, False)

    # Return a list of all the filled adjacent squares to the given square
    def getFilledAdj(self, coords):
        return self.getAdj(coords, True)

    # Return a list of either filled or emtpy adjacent squares to square
    def getAdj(self, coords, filled):
        adj = [] # list of adj squares
        # Loop through rows
        for i in range(coords[0] - 1, coords[0] + 2):
            # Check row in bounds of board
            if i < 0 or i > 7: continue
            # Loop through cols
            for j in range(coords[1] - 1, coords[1] + 2):
                if j < 0 or j > 7: continue # Check col in board
                if filled and self.board[i,j] != Piece.NONE.value:
                    toAdd = (i,j)
                    adj.append(toAdd)
                if not filled and self.board[i,j] == Piece.NONE.value:
                    toAdd = (i, j)
                    adj.append(toAdd)
        return adj

    # Return the score of a player
    def getScore(self, turn):
        score = 0
        for slot in np.nditer(self.board):
            if Piece[turn.name].value == slot:
                score = score + 1
        return score

    # Update the board with a given move
    def update(self, move, turn):

        # Populate new square
        self.board[move[0], move[1]] = Piece[turn.name].value
        toRev = (move[0], move[1])
        self.empty_adj.remove(toRev)  # Remove newly populated square from adj empty

        # Add all of the new empty adj squares
        for sqr in self.getEmptyAdj(move):
            if sqr not in self.empty_adj:
                self.empty_adj.append(sqr)

        # Convert each line necessary
        for sqr in self.getFilledAdj(move):
            self.convertLine(turn, move, [sqr[0] - move[0], sqr[1] - move[1]])

    # Flip the color of a specified line if valid move
    def convertLine(self, turn, move, dir):
        lookingFor = Piece.WHITE.value if turn == Turn.WHITE else Piece.BLACK.value
        toConvert = []
        converted = False
        i = move[0]
        j = move[1]
        while not converted:
            i += dir[0]  # Current square to consider
            j += dir[1]
            if i < 0 or i > 7 or j < 0 or j > 7 or self.board[i, j] == Piece.NONE.value: break
            if self.board[i, j] == lookingFor:
                converted = True
                for piece in toConvert:  # Convert line
                    self.board[piece[0], piece[1]] = lookingFor
            else:
                toConvert.append([i,j])

    # Print the current game board to stdout
    def printBoard(self):
        print("    0   1   2   3   4   5   6   7  ")
        for i in range(0,8):
            print(i,"|", end="")
            for j in range(0,8):
                toPrint = "  "
                if self.board[i,j] == Piece.WHITE.value:
                    toPrint = " O"
                elif self.board[i,j] == Piece.BLACK.value:
                    toPrint = " X"
                print(toPrint,"|",end="")
            print("") # Newline
