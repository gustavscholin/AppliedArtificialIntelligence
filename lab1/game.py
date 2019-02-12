from enum import Enum
import numpy as np
from board import Board


class Turn(Enum):
    WHITE = 0
    BLACK = 1

class Game:

    def __init__(self, player_w, player_b):
        self.players[0] = player_w
        self.players[1] = player_b
        self.board = Board()
        self.turn = Turn.BLACK

    def start(self):
        while self.board.validMoves(self.turn):
            curr_move = self.players[self.turn].getMove(self.board)
            self.board.update(curr_move, self.turn)
            self.turn = Turn.WHITE if self.turn else Turn.BLACK