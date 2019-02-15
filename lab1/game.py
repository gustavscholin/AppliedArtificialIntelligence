import time

from lab1.board import Board
from lab1.board import Color

class Game:

    # Init the game with players and a board
    def __init__(self, player_w, player_b):
        self.players = []
        self.players.append(player_w)
        self.players.append(player_b)
        self.board = Board()
        self.turn = Color.BLACK

    # Start the game and execute until a winner emerges
    def start(self):
        print("GAME START")
        while self.board.validMoves(self.turn):
            self.board.printBoard()
            t = time.time()
            curr_move = self.players[self.turn.value].getMove(self.board)
            print('Move time: ' + str(time.time() - t))
            self.board.update(curr_move, self.turn)
            self.turn = Color.WHITE if self.turn.value else Color.BLACK
        print("GAME ENDED")
        print()
        self.board.printBoard()
        print()
        print('White: ' + str(self.board.getScore(Color.WHITE)))
        print('Black: ' + str(self.board.getScore(Color.BLACK)))
