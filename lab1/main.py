from lab1.board import Color
from lab1.player import HumanPlayer
from lab1.game import Game

player1 = HumanPlayer(Color.WHITE)
player2 = HumanPlayer(Color.BLACK)

game = Game(player1, player2)
game.start()
