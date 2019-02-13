from lab1.board import Board, Turn

print("THIS IS MAIN")

board = Board()

print(board)
print()
move = (2,2)
board.update(move, Turn.WHITE)

print(board)

print(board.getScore(Turn.BLACK))
