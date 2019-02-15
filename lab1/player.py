import copy
import sys
import time
from random import randint

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

    def __init__(self, color, depth):
        super().__init__(color)
        self.depth = depth

    # Implementation of the minimax algorithm with alpha-beta pruning and depth constrain
    def getMove(self, board):
        print(board.validMoves(self.color))
        print(self.color.name)

        # Establish the colors of the players
        op_color = Color.BLACK
        if self.color == op_color:
            op_color = Color.WHITE

        def minValue(board, alpha, beta, depth):
            actions = board.validMoves(op_color)
            if not actions or depth > self.depth:
                return board.getScore(self.color)

            v = sys.maxsize
            for a in actions:
                new_board = copy.deepcopy(board)
                new_board.update(a, op_color)
                v = min(v, maxValue(new_board, alpha, beta, depth + 1))
                if v <= alpha:
                    return v
                beta = min(beta, v)
            return v

        def maxValue(board, alpha, beta, depth):
            actions = board.validMoves(self.color)
            if not actions or depth > self.depth:
                return board.getScore(op_color)

            v = -sys.maxsize
            for a in actions:
                new_board = copy.deepcopy(board)
                new_board.update(a, self.color)
                v = max(v, minValue(new_board, alpha, beta, depth + 1))
                if v >= beta:
                    return v
                alpha = max(alpha, v)
            return v

        # Check if a move is in a corner square
        def isCornerMove(move):
            corners = [(0,0), (0,7), (7,0), (7,7)]
            if move in corners:
                return True
            return False

        # Check if a move is in a square surrounding a corner
        def isXMove(move):
            x_moves = [(1,0), (0,1), (1,1), (0,6), (1,7), (6,1), (6,0), (7,1), (6,1), (6,7), (7,6), (6,6)]
            if move in x_moves:
                return True
            return False

        # Get all valid moves and returns the move that maximizing minValue
        actions = board.validMoves(self.color)
        action_values = []
        for a in actions:
            new_board = copy.deepcopy(board)
            new_board.update(a, self.color)
            action_values.append(minValue(new_board, -sys.maxsize, sys.maxsize, 1))

            # Corner moves are rewarded and moves in squares surrounding corners are penalized
            if isCornerMove(a):
                action_values[-1] = 2 * action_values[-1]
            elif isXMove(a):
                action_values[-1] = 0.5 * action_values[-1]
        return actions[action_values.index(max(action_values))]


# Player class to allow for a human to play the game from the terminal
class HumanPlayer(Player):

    # Get the next move from the human player
    def getMove(self, board):
        print(str(board.validMoves(self.color)) + '\n')
        valid_input = False
        move = ()

        # Parse the move and check if it is valid
        while not valid_input:
            user_input = input('What is your move?\n')
            if len(user_input.split()) != 2:
                print('Invalid input')
            else:
                try:
                    numbers = []
                    for x in user_input.split():
                        numbers.append(int(x))
                except ValueError:
                    print('Invalid input')
                else:
                    move = tuple(numbers)
                    if move in board.validMoves(self.color):
                        valid_input = True
                    else:
                        print('Invalid move')

        return move
