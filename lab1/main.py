from lab1.board import Turn, Board
from lab1.player import HumanPlayer
from lab1.game import Game

#player1 = HumanPlayer(Turn.WHITE)
#player2 = HumanPlayer(Turn.BLACK)

#game = Game(player1, player2)
#game.start()


board = Board()
board.printBoard()
blackMoves = board.validMoves(Turn.BLACK)
whiteMoves = board.validMoves(Turn.WHITE)

board.update((2, 3), Turn.BLACK)
board.printBoard()
