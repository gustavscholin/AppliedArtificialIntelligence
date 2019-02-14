from lab1.board import Board, Color
from lab1.player import HumanPlayer

# print("THIS IS MAIN")
#
board = Board()
board.printBoard()
# move = (2,2)
# board.update(move, Turn.WHITE)
#
# board.printBoard()
#
# print(board.getScore(Turn.BLACK))

p1 = HumanPlayer(Color.WHITE)
move = p1.getMove(board)
print(move)
