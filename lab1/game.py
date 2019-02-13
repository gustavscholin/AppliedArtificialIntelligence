from lab1.board import Board
from lab1.board import Turn

class Game:

    # Init the game with players and a board
    def __init__(self, player_w, player_b):
        self.players[0] = player_w
        self.players[1] = player_b
        self.board = Board()
        self.turn = Turn.BLACK

    # Start the game and execute until a winner emerges
    def start(self):
        while self.board.validMoves(self.turn):
            curr_move = self.players[self.turn].getMove(self.board)
            self.board.update(curr_move, self.turn)
            self.turn = Turn.WHITE if self.turn else Turn.BLACK
        print("GAME ENDED")