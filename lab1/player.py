import copy

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

    def getMove(self, board):
        actions = board.validMoves(self.color)
        action_values = []
        for a in actions:
            new_board = copy.deepcopy(board)
            new_board.update(a, self.color)
            action_values.append(self.minValue(new_board, -1000, 1000))

        return actions[action_values.index(max(action_values))]

    def maxValue(self, board, alpha, beta):
        actions = board.validMoves(self.color)
        if not actions:
            return board.getScore(self.color)

        v = -1000
        for a in actions:
            new_board = copy.deepcopy(board)
            new_board.update(a, self.color)
            v = max(v, self.minValue(new_board, alpha, beta))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def minValue(self, board, alpha, beta):
        op_color = Turn.BLACK
        if self.color == op_color:
            op_color = Turn.WHITE

        actions = board.validMoves(op_color)
        if not actions:
            return board.getScore(op_color)

        v = 1000
        for a in actions:
            new_board = copy.deepcopy(board)
            new_board.update(a, op_color)
            v = min(v, self.maxValue(new_board, alpha, beta))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v





# Player class to allow for a human to play the game from the terminal
class HumanPlayer(Player):

    def getMove(self, board):
        print("HUMAN PLAYER")
        toRet = (0, 0)
        return toRet
