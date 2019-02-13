import copy
import sys

from lab1.board import Turn


class Player:

    # Init the player with their color
    def __init__(self, color):
        self.color = color

    # Get the next move from this player given the current board
    def getMove(self, board):
        print("SHOULD BE OVERRIDEN")
        toRet = (0, 0)
        return toRet


# Class representing a computer player
class AIPlayer(Player):

    def getMove(self, board, d = 4):
        op_color = Turn.BLACK
        if self.color == op_color:
            op_color = Turn.WHITE

        actions = board.validMoves(self.color)
        action_values = []
        for a in actions:
            new_board = copy.deepcopy(board)
            new_board.update(a, self.color)
            action_values.append(self.minValue(new_board, -sys.maxsize, sys.maxsize, 1, self.color))

        def maxValue(board, alpha, beta, depth, color):
            actions = board.validMoves(color)
            if not actions or depth > d:
                return board.getScore(color)

            v = -sys.maxsize
            for a in actions:
                new_board = copy.deepcopy(board)
                new_board.update(a, color)
                v = max(v, minValue(new_board, alpha, beta, depth + 1, op_color))
                if v >= beta:
                    return v
                alpha = max(alpha, v)
            return v

        def minValue(board, alpha, beta, depth, color):
            actions = board.validMoves(op_color)
            if not actions or depth > d:
                return board.getScore(op_color)

            v = sys.maxsize
            for a in actions:
                new_board = copy.deepcopy(board)
                new_board.update(a, op_color)
                v = min(v, maxValue(new_board, alpha, beta, depth + 1, self.color))
                if v <= alpha:
                    return v
                beta = min(beta, v)
            return v

        return actions[action_values.index(max(action_values))]


# Player class to allow for a human to play the game from the terminal
class HumanPlayer(Player):

    def getMove(self, board):
        print("HUMAN PLAYER")
        toRet = (0, 0)
        return toRet
