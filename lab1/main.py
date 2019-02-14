from lab1.board import Turn
from lab1.player import HumanPlayer
from lab1.game import Game

player1 = HumanPlayer(Turn.WHITE)
player2 = HumanPlayer(Turn.BLACK)

game = Game(player1, player2)
game.start()
