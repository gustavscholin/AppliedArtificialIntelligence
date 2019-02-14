import copy
import sys

from lab1.board import Color


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
        op_color = Color.BLACK
        if self.color == op_color:
            op_color = Color.WHITE

        actions = board.validMoves(self.color)
        action_values = []
        for a in actions:
            new_board = copy.deepcopy(board)
            new_board.update(a, self.color)
            action_values.append(self.minValue(new_board, -sys.maxsize, sys.maxsize, 1, self.color))

        def maxValue(board, alpha, beta, depth):
            actions = board.validMoves(self.color)
            if not actions or depth > d:
                return board.getScore(self.color)

            v = -sys.maxsize
            for a in actions:
                new_board = copy.deepcopy(board)
                new_board.update(a, self.color)
                v = max(v, minValue(new_board, alpha, beta, depth + 1, op_color))
                if v >= beta:
                    return v
                alpha = max(alpha, v)
            return v

        def minValue(board, alpha, beta, depth):
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
        valid_input = False
        move = ()
        while not valid_input:
            user_input = input('What is your move?')
            if len(user_input.split()) != 2:
                print('Invalid input')
            else:
                try:
                    numbers = (int(x) for x in user_input.split())
                except ValueError:
                    print('Invalid input')
                else:
                    move = tuple(numbers)
                    if (move in board.validMoves(self.color)):
                        valid_input = True
                    else:
                        print('Invalid move')
        return move
